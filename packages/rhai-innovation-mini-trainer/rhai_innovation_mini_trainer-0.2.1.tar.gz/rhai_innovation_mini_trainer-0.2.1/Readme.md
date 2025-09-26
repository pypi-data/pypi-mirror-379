# Mini Trainer

[![PR Tests](https://github.com/Red-Hat-AI-Innovation-Team/mini_trainer/actions/workflows/pr-tests.yml/badge.svg)](https://github.com/Red-Hat-AI-Innovation-Team/mini_trainer/actions/workflows/pr-tests.yml)

MiniTrainer is a small form factor and extremely efficient training library for models up to 70B parameters on a single 8xA100/H100 node, although it supports multinode training if your infrastructure has ROCE/Infiniband.

### Features:
- [Liger Kernels](https://github.com/linkedin/Liger-Kernel/tree/908b89c4dc9bb872351887b382a1e09ca25fbe85) to minimize memory footprint by chunking the loss computation.
- **Optional Orthogonal Subspace Learning (OSL)** via SVD-based decomposition and constrained subspace optimization for continual fine-tuning and low-rank adaptation.
- **Automatic minibatching with high-performance LPT packing** based on the effective batch size: forget about tuning your gradient accumulation, just specify `max-tokens-per-gpu` and `batch-size` and the library will automatically divides your batches in balanced minibatches across your GPUs using numba-optimized LPT (Longest Processing Time) algorithm for optimal load balancing and speed.
- **FullyShardedDataParallel (FSDP2)** via native PyTorch `torch.distributed.fsdp` for efficient sharding across multi-GPU settings (no accelerate).
- **Padding-free** -- it currently only works on GPUs that support flash attention and uses the padding-free feature of the transformer library to avoid extra computation on padding tokens.
- **Infinite Sampling** -- forget about setting the number of epochs, just start the training and it would automatically sample an infinite stream of batches from your data.
- **pretrain and supervised** fine tuninng tokenization schemes
- **`jsonl` logging**, your metrics will be logged in the output directory as a jsonl that can easily be processed for plotting, wandb or whatever you like for experiment tracking.

### 🔥 What's New (July-02-2025) - High-Performance Batch Packing

- **Orthogonal Subspace Learning (OSFT)** mode: allows fine-tuning in a parameter-efficient low-rank subspace while freezing parts of the core model that need to be preserved for continual learning scenarios. Controlled via `--osft` flag.
- **Numba-Optimized LPT Batch Packing**: Implemented high-performance LPT (Longest Processing Time) algorithm with JIT compilation for optimal load balancing across GPUs. Achieves 3.5x better speed than greedy while providing up to 217% better load balance, 60-89% lower variance, and 33% fewer minibatches.
- **Comprehensive test suite**: Added extensive testing framework in `tests/` folder with realistic outlier scenarios and performance benchmarks.

### 🚀 What's New (May-16-2025)

- Removed `accelerate` dependency and switched to native PyTorch FSDP2 (`torch.distributed.fsdp`).
- Simplified metrics via new `BatchMetrics` (instance-scoped counters).
- Streamlined CLI: dropped `--fsdp-sharding-strategy` flag.
- Now saving the checkpoints in bf16 so we don't use double the size of the models that were loaded.

# Installation

## Using uv (Recommended)

```shell
# Regular installation
uv sync

# Install with flash-attention support (flash-attn installed separately due to build dependencies)
uv sync
uv pip install .[cuda]

# For editing this codebase, install with -e (editable)
uv pip install -e .
uv pip install -e .[cuda]
```

## Using pip

```shell
# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Regular installation
pip install .
pip install .[cuda]

# For editing this codebase, install with -e (editable)
pip install -e .
pip install -e .[cuda]
```

# Data Tokenization

This utility also supports **multiturn conversations**: `process_data.py` can handle sequences of `user` and `assistant` messages of any length, correctly masking only assistant responses across multiple turns.

You first need to tokenize your data and get the input tokens and the output label tokens. The resulting label tokens will contain a mask token (`-100`) for the `user` and `system` roles, and unmask the tokens for the `assistant` role content. If you wish to pretrain (i.e. train on all tokens in the input) include the data in a single `pretrain` role message.

```shell
TOKENIZERS_PARALLELISM=False \
python process_data.py \
--input-file "/workspace/home/lab/training_data_new.jsonl" \
--output-file "tokenized_data.jsonl" \
--model-name-or-path "Qwen/Qwen2.5-1.5B-instruct" \
--max-sample-num-tokens 128000
```

### Data Assumptions
The data must be a `json list` format (each line a json), and each sample should have a `messages` field formatted like this:


```json
{"messages": [{"role": "user","content": "<input 1>"},{"role": "assistant","content": "<output 1>"}]}
{"messages": [{"role": "user","content": "<input 2>"},{"role": "assistant","content": "<output 2>"}]}
{"messages": [{"role": "pretrain","content": "<pretrain data>"}]} #this sample will have completely unmasked tokens in the labels.
```

the data processing script will populate `input_ids`, `labels` and the sample length in the `len` keys. To do so the data processor uses the chat template included in the tokenizer, make sure the tokenizer has a proper chat template set up.

NOTE: check the printed examples at the end and make sure the samples look properly formatted and that the masked part of the labels correspods to anything that the model would not learn to generate (although it would still condition the model -- the $x$ in $p(y|x)$ ).

## Pretraining
if you want to pretrain on some samples, such samples should have a messages format with a single element with the role `pretrain` and the data in the `content` key. This would use void using the chat template and the complete string in the `content` key would be unmasked.

## launch training

all training parameters can be found in [train.py](./train.py). Make sure to use the tokenized data created above as the input here.

```shell
torchrun --nnodes=1 --nproc-per-node=8 train.py \
        --output-dir /new_data/aldo/balrog_test \
        --data-path ./tokenized_data.jsonl \
        --model-name-or-path Qwen/Qwen2.5-1.5B-instruct \
        --min-samples-per-checkpoint 2000 \
        --num-warmup-steps 20 \
        --max-tokens-per-gpu 128000 \
        --batch-size 128 \
        --use-liger-kernels \
        --seed 893 \
        --learning-rate 6e-6
```

The parameters used for the run will be saved in `<output_dir>/training_params.json` and the metrics will be saved to `<output_dir>/training_metrics_0.jsonl`.

NOTE: keep an eye on `nvidia-smi` or `nvtop` while training and raise the `max-tokens-per-gpu` until you're close (but not quite to avoid cuda memory re allocations) to the max memory in your GPUs.

## Continual Learning / OSFT

mini_trainer also supports a novel technique for continual learning known as **Orthogonal Subspace Fine-Tuning**, or OSFT for short.

This method allows you to target the pieces of your language model which are least likely to contain valuable task-specific information. 

To run this method with `mini_trainer`, simply pass the `--osft` flag to enable the technique, and pass the `--osft-unfreeze-rank-ratio` parameter to specify how much of the model's most important pieces you would like to remain frozen (where a value of 0.0 means everything is frozen, and 1.0 means we train all of the singular values).

```bash
torchrun --nnodes=1 --nproc-per-node=8 train.py \
        --output-dir /new_data/aldo/balrog_test \
        --data-path ./tokenized_data.jsonl \
        --model-name-or-path Qwen/Qwen2.5-1.5B-instruct \
        --min-samples-per-checkpoint 2000 \
        --num-warmup-steps 20 \
        --max-tokens-per-gpu 128000 \
        --batch-size 128 \
        --use-liger-kernels \
        --seed 893 \
        --learning-rate 6e-6 \
        --osft \
        --osft-unfreeze-rank-ratio 0.25  # trains the 25% of the model which give the least amount of information

```

### Multinode Training

First, you need to know the IP address of the node with rank 0. 

```shell
# identify the main ethernet interface
ip route get 1.1.1.1 | awk '{print $5}'
# eth0
# use the outpput of this command to get the ip address of such node
export master_addr=$(ip addr show eth0 | grep "inet\b" | awk '{print $2}' | cut -d/ -f1)
echo $master_addr
# 10.241.128.19
# set some free port in the node
export master_port=29500
```

Make sure your tokenized `data-path` and your `output-dir` are both in a shared file system and then on each node do:

```shell
export num_nodes=2 # set this to the number of nodes you're using
torchrun --nnodes=$num_nodes --node_rank=$rank --nproc_per_node=8 --rdzv_id=101 \
        --rdzv_endpoint="$master_addr:$master_port" train.py \
        --output-dir ./experiment_checkpoints_loggin_etc/ \
        --data-path ./tokenized_data.jsonl \
        --model-name-or-path Qwen/Qwen2.5-1.5B-instruct \
        --min-samples-per-checkpoint 10000 \
        --num-warmup-steps 20 \
        --max-tokens-per-gpu 60000 \
        --batch-size 128 \
        --use-liger-kernels \
        --seed 893 \
        --learning-rate 6e-6
```

NOTE: the number of nodes and the rank have to be set by the launcher or manually on each node.

### Multi-Node Training via SLURM

Create a file `slurm_multi_node.sbatch`:

```bash
#!/bin/bash
#SBATCH --job-name=minitrain-multinode   # job name
#SBATCH --output=minitrain_%j.log        # stdout log
#SBATCH --partition=gpu                  # adjust for your cluster
#SBATCH -N 2                             # number of nodes
#SBATCH --ntasks-per-node=8              # GPUs per node
#SBATCH --gpus-per-task=1                # GPUs per task
#SBATCH --cpus-per-task=10               # CPU cores per task
#SBATCH --time=24:00:00                  # walltime

export MASTER_ADDR=$(scontrol show hostnames "$SLURM_JOB_NODELIST" | head -n1)
export MASTER_PORT=29500

srun torchrun \
  --nnodes=$SLURM_JOB_NUM_NODES \
  --nproc-per-node=$SLURM_NTASKS_PER_NODE \
  --node_rank=$SLURM_NODEID \
  --rdzv_id=$SLURM_JOB_ID \
  --rdzv_backend=c10d \
  --rdzv_endpoint=${MASTER_ADDR}:${MASTER_PORT} \
  train.py \
    --output-dir ./checkpoints/ \
    --data-path ./tokenized_data.jsonl \
    --max-tokens-per-gpu 60000 \
    --batch-size 128
```

Submit with:

```bash
sbatch slurm_multi_node.sbatch
```

Adjust the SBATCH directives and paths (`train.py`, `--data-path`, `--output-dir`) as needed.

* For a full torchrun + SLURM example, see the PyTorch official tutorial:
  https://github.com/pytorch/examples/blob/main/distributed/ddp-tutorial-series/slurm/sbatch_run.sh

# Testing

The project uses tox with uv for fast, isolated testing across multiple Python versions. Tests are located in the `tests/` directory and provide comprehensive coverage of:

- **Data Pipeline**: Dataset loading, sampling, batching, and collation
- **Model Setup**: Initialization, FSDP wrapping, optimizer configuration, and Liger kernels
- **Training Loop**: Forward/backward passes, gradient accumulation, and checkpointing
- **Distributed Training**: Multi-rank coordination, metrics reduction, and synchronization
- **Batch Packing**: Performance comparisons between greedy and LPT algorithms
- **Utilities**: Logging, memory management, and configuration handling

## Quick Testing

```shell
# Run all tests
uv run tox -e test

# Run tests with verbose output
uv run tox -e test-verbose

# Run until first failure (fast feedback)
uv run tox -e test-quick

# Run with coverage report
uv run tox -e test-coverage
```

## Multi-Python Testing

```shell
# Test on Python 3.11
uv run tox -e py311

# Test on Python 3.12  
uv run tox -e py312

# Test on all supported Python versions
uv run tox
```

## Code Quality

```shell
# Check code style with ruff
uv run tox -e lint

# Fix linting issues automatically
uv run tox -e lint-fix

# Format code
uv run tox -e format

# Check if code is formatted
uv run tox -e format-check
```

## Running Specific Tests

```shell
# Run specific test file
uv run tox -e test -- tests/test_batch_lengths_to_minibatches.py

# Run specific test class
uv run tox -e test -- tests/test_batch_lengths_to_minibatches.py::TestBatchLengthsToMinibatches

# Run specific test method
uv run tox -e test-quick -- tests/test_batch_lengths_to_minibatches.py::TestBatchLengthsToMinibatches::test_empty_batch
```

## Legacy Test Runner

For comprehensive batch packing performance analysis:

```shell
cd tests && python run_tests.py
```

