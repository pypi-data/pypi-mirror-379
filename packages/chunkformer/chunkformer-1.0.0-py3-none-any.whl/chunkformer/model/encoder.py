# Copyright (c) 2021 Mobvoi Inc (Binbin Zhang, Di Wu)
#               2022 Xingchen Song (sxc19@mails.tsinghua.edu.cn)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# Modified from ESPnet(https://github.com/espnet/espnet)

"""Encoder definition."""
from typing import List, Optional, Tuple

import torch

from .attention import ChunkAttentionWithRelativeRightContext
from .convolution import ChunkConvolutionModule
from .embedding import RelPositionalEncodingWithRightContext
from .encoder_layer import ChunkFormerEncoderLayer
from .positionwise_feed_forward import PositionwiseFeedForward
from .subsampling import DepthwiseConvSubsampling
from .utils.common import get_activation
from .utils.mask import make_pad_mask


class ChunkFormerEncoder(torch.nn.Module):
    """ChunkFormer encoder module."""

    def __init__(
        self,
        input_size: int,
        output_size: int = 256,
        attention_heads: int = 4,
        linear_units: int = 2048,
        num_blocks: int = 6,
        dropout_rate: float = 0.1,
        positional_dropout_rate: float = 0.1,
        attention_dropout_rate: float = 0.0,
        input_layer: str = "dw_striding",
        pos_enc_layer_type: str = "chunk_rel_pos",
        normalize_before: bool = True,
        static_chunk_size: int = 0,
        use_dynamic_chunk: bool = False,
        global_cmvn: Optional[torch.nn.Module] = None,
        use_dynamic_left_chunk: bool = False,
        macaron_style: bool = True,
        selfattention_layer_type: str = "chunk_rel_seflattn",
        activation_type: str = "swish",
        use_cnn_module: bool = True,
        cnn_module_kernel: int = 15,
        causal: bool = False,
        cnn_module_norm: str = "batch_norm",
        dynamic_conv: bool = False,
        layer_norm_type: str = "layer_norm",
        gradient_checkpointing: bool = False,
        final_norm: bool = True,
        norm_eps: float = 1e-5,
        use_sdpa: bool = False,
        dynamic_chunk_sizes: Optional[List] = None,
        dynamic_left_context_sizes: Optional[List] = None,
        dynamic_right_context_sizes: Optional[List] = None,
    ):
        """Construct ChunkFormerEncoder

        Args:
            input_size to use_dynamic_chunk, see in BaseEncoder
            positionwise_conv_kernel_size (int): Kernel size of positionwise
                conv1d layer.
            macaron_style (bool): Whether to use macaron style for
                positionwise layer.
            selfattention_layer_type (str): Encoder attention layer type,
                the parameter has no effect now, it's just for configure
                compatibility.
            activation_type (str): Encoder activation function type.
            use_cnn_module (bool): Whether to use convolution module.
            cnn_module_kernel (int): Kernel size of convolution module.
            causal (bool): whether to use causal convolution or not.
            dynamic_chunk_sizes (list): List of chunk sizes for dynamic chunking.
            dynamic_left_context_sizes (list): List of left context sizes for
                dynamic chunking.
            dynamic_right_context_sizes (list): List of right context sizes for
                dynamic chunking.
        """
        torch.nn.Module.__init__(self)
        assert selfattention_layer_type == "chunk_rel_seflattn"
        assert pos_enc_layer_type == "chunk_rel_pos"
        assert input_layer == "dw_striding"

        self._output_size = output_size
        self.global_cmvn = global_cmvn

        assert layer_norm_type in ["layer_norm", "rms_norm"]
        self.normalize_before = normalize_before
        self.final_norm = final_norm

        self.static_chunk_size = static_chunk_size
        self.use_dynamic_chunk = use_dynamic_chunk
        self.use_dynamic_left_chunk = use_dynamic_left_chunk
        self.gradient_checkpointing = gradient_checkpointing
        self.use_sdpa = use_sdpa

        self._output_size = output_size
        self.global_cmvn = global_cmvn
        # NOTE(Mddct): head_dim == output_size // attention_heads for most of
        #    speech tasks,  but for other task (LLM),
        #    head_dim == hidden_size * attention_heads. refactor later

        assert layer_norm_type in ["layer_norm", "rms_norm"]
        self.normalize_before = normalize_before
        self.final_norm = final_norm
        self.after_norm = torch.nn.LayerNorm(output_size * 1, eps=1e-5)

        self.static_chunk_size = static_chunk_size
        self.use_dynamic_chunk = use_dynamic_chunk
        self.use_dynamic_left_chunk = use_dynamic_left_chunk
        self.gradient_checkpointing = gradient_checkpointing

        self.dynamic_chunk_sizes = dynamic_chunk_sizes
        self.dynamic_left_context_sizes = dynamic_left_context_sizes
        self.dynamic_right_context_sizes = dynamic_right_context_sizes

        self.cnn_module_kernel = cnn_module_kernel
        activation = get_activation(activation_type)
        self.num_blocks = num_blocks
        self.dynamic_conv = dynamic_conv
        self.input_size = input_size
        self.attention_heads = attention_heads

        self.embed = DepthwiseConvSubsampling(
            subsampling=input_layer,
            subsampling_rate=8,
            feat_in=input_size,
            feat_out=output_size,
            conv_channels=output_size,
            pos_enc_class=RelPositionalEncodingWithRightContext(
                output_size, positional_dropout_rate
            ),
            subsampling_conv_chunking_factor=1,
            activation=torch.nn.ReLU(),
        )

        encoder_selfattn_layer = ChunkAttentionWithRelativeRightContext
        encoder_selfattn_layer_args = (
            attention_heads,
            output_size,
            attention_dropout_rate,
        )

        # feed-forward module definition
        positionwise_layer = PositionwiseFeedForward
        positionwise_layer_args = (
            output_size,
            linear_units,
            dropout_rate,
            activation,
        )
        # convolution module definition
        convolution_layer = ChunkConvolutionModule
        convolution_layer_args = (
            output_size,
            cnn_module_kernel,
            activation,
            cnn_module_norm,
            causal,
            True,
            dynamic_conv,
        )

        self.encoders = torch.nn.ModuleList(
            [
                ChunkFormerEncoderLayer(
                    size=output_size,
                    self_attn=encoder_selfattn_layer(*encoder_selfattn_layer_args),
                    feed_forward=positionwise_layer(*positionwise_layer_args),
                    feed_forward_macaron=(
                        positionwise_layer(*positionwise_layer_args) if macaron_style else None
                    ),
                    conv_module=(
                        convolution_layer(*convolution_layer_args) if use_cnn_module else None
                    ),
                    dropout_rate=dropout_rate,
                    normalize_before=normalize_before,
                )
                for _ in range(num_blocks)
            ]
        )

    def forward_parallel_chunk(
        self,
        xs,
        xs_origin_lens,
        chunk_size: int = -1,
        left_context_size: int = -1,
        right_context_size: int = -1,
        att_cache: torch.Tensor = torch.zeros((0, 0, 0)),
        cnn_cache: torch.Tensor = torch.zeros((0, 0)),
        truncated_context_size: int = 0,
        offset: torch.Tensor = torch.zeros(0),
    ) -> Tuple[torch.Tensor, torch.Tensor, List, torch.Tensor, torch.Tensor, torch.Tensor]:
        """Embed positions in tensor.

        Args:
            xs: list of B input tensors (T, D)
            xs_lens: input length (B)
            decoding_chunk_size: decoding chunk size for dynamic chunk
                0: default for training, use random dynamic chunk.
                <0: for decoding, use full chunk.
                >0: for decoding, use fixed chunk size as set.
            num_decoding_left_chunks: number of left chunks, this is for decoding,
            the chunk size is decoding_chunk_size.
                >=0: use num_decoding_left_chunks
                <0: use all left chunks
        Returns:
            encoder output tensor xs, and subsampled masks
            xs: padded output tensor (B, T' ~= T/subsample_rate, D)
            masks: torch.Tensor batch padding mask after subsample
                (B, 1, T' ~= T/subsample_rate)
        """
        if offset.shape[0] == 0:
            offset = torch.zeros(len(xs), dtype=torch.long, device=xs_origin_lens.device)

        # --------------------------Masked Batching----------------------------------
        subsampling = self.embed.subsampling_rate
        context = self.embed.right_context + 1  # Add current frame
        size = (chunk_size - 1) * subsampling + context
        step = subsampling * chunk_size
        device = xs_origin_lens.device

        conv_lorder = self.cnn_module_kernel // 2

        upper_bounds_att = []  # type: List[torch.Tensor]
        lower_bounds_att = []  # type: List[torch.Tensor]
        upper_bounds_conv = []  # type: List[torch.Tensor]
        lower_bounds_conv = []  # type: List[torch.Tensor]
        x_pad = []  # type: List[torch.Tensor]
        xs_lens = []  # type: List[int]
        n_chunks = []  # type: List[int]
        for xs_origin_len, x, offs in zip(xs_origin_lens, xs, offset):
            x = x.to(device)

            # padding for unfold
            if x.size(0) >= size:
                n_frames_pad = (step - ((x.size(0) - size) % step)) % step
            else:
                n_frames_pad = size - x.size(0)
            x = torch.nn.functional.pad(x, (0, 0, 0, n_frames_pad))  # (T, 80)
            n_chunk = ((x.size(0) - size) // step) + 1
            x = x.unfold(0, size=size, step=step)  # [n_chunk, 80, size]
            x = x.transpose(2, 1)

            # attention boundaries
            max_len = 1 + (xs_origin_len - context) // subsampling
            upper_bound_att = (
                chunk_size
                + right_context_size
                + torch.arange(
                    0,
                    1 + (xs_origin_len + n_frames_pad - context) // subsampling,
                    1 + (size - context) // subsampling,
                    device=device,
                )
            )
            lower_bound_att = upper_bound_att - max_len
            upper_bound_att += offs

            # convolution boundaries
            upper_bound_conv = (
                chunk_size
                + conv_lorder
                + torch.arange(
                    0,
                    1 + (xs_origin_len + n_frames_pad - context) // subsampling,
                    1 + (size - context) // subsampling,
                    device=device,
                )
            )
            lower_bound_conv = torch.maximum(
                upper_bound_conv - max_len,
                torch.full_like(upper_bound_conv, conv_lorder - right_context_size),
            )
            upper_bound_conv += offs

            xs_lens += [size] * (n_chunk - 1) + [size - n_frames_pad]
            upper_bounds_att.append(upper_bound_att)
            lower_bounds_att.append(lower_bound_att)
            upper_bounds_conv.append(upper_bound_conv)
            lower_bounds_conv.append(lower_bound_conv)
            x_pad.append(x)
            n_chunks.append(n_chunk)

        xs = torch.cat(x_pad, dim=0).to(device)
        xs_lens = torch.tensor(xs_lens).to(device)  # type: ignore
        masks = ~make_pad_mask(xs_lens, xs.size(1)).unsqueeze(1)  # type: ignore  # (B, 1, T)
        upper_bounds_att = torch.cat(upper_bounds_att).unsqueeze(1).to(device)  # type: ignore
        lower_bounds_att = torch.cat(lower_bounds_att).unsqueeze(1).to(device)  # type: ignore
        upper_bounds_conv = torch.cat(upper_bounds_conv).unsqueeze(1).to(device)  # type: ignore
        lower_bounds_conv = torch.cat(lower_bounds_conv).unsqueeze(1).to(device)  # type: ignore

        # forward model
        if self.global_cmvn is not None:
            xs = self.global_cmvn(xs)

        xs, pos_emb, masks = self.embed(
            xs,
            masks,
            chunk_size=chunk_size,
            left_context_size=left_context_size,
            right_context_size=right_context_size,
        )
        # convolution mask
        # [B, left_context_size + chunksize]
        mask_pad = (
            torch.arange(0, conv_lorder + chunk_size + conv_lorder, device=masks.device)
            .unsqueeze(0)
            .repeat(xs.size(0), 1)
        )
        mask_pad = (lower_bounds_conv <= mask_pad) & (mask_pad < upper_bounds_conv)
        mask_pad = mask_pad.flip(-1).unsqueeze(1)

        # attention mask
        # [B, left_context_size + chunksize]
        att_mask = (
            torch.arange(
                0, left_context_size + chunk_size + right_context_size, device=masks.device
            )
            .unsqueeze(0)
            .repeat(xs.size(0), 1)
        )
        att_mask = (lower_bounds_att <= att_mask) & (att_mask < upper_bounds_att)
        att_mask = att_mask.flip(-1).unsqueeze(1)

        r_att_cache = []  # type: List[torch.Tensor]
        r_cnn_cache = []  # type: List[torch.Tensor]
        att_cache = att_cache.to(device)
        cnn_cache = cnn_cache.to(device)

        for i, layer in enumerate(self.encoders):
            xs, _, new_att_cache, new_cnn_cache = layer.forward_parallel_chunk(
                xs,
                att_mask,
                pos_emb,
                mask_pad=mask_pad,
                right_context_size=right_context_size,
                left_context_size=left_context_size,
                att_cache=att_cache[i] if att_cache.size(0) > 0 else att_cache,
                cnn_cache=cnn_cache[i] if cnn_cache.size(0) > 0 else cnn_cache,
                truncated_context_size=truncated_context_size,
            )

            r_att_cache.append(new_att_cache)
            r_cnn_cache.append(new_cnn_cache)

        del att_cache
        del cnn_cache
        if self.normalize_before:
            xs = self.after_norm(xs)

        xs_lens = self.embed.calc_length(xs_origin_lens)
        offset += xs_lens

        # NOTE(xcsong): shape(r_att_cache) is (elayers, head, ?, d_k * 2),
        #   ? may be larger than cache_t1, it depends on required_cache_size
        r_att_cache: torch.Tensor = torch.stack(r_att_cache, dim=0)  # type: ignore
        # NOTE(xcsong): shape(r_cnn_cache) is (e, b=1, hidden-dim, cache_t2)
        r_cnn_cache: torch.Tensor = torch.stack(r_cnn_cache, dim=0)  # type: ignore
        return xs, xs_lens, n_chunks, r_att_cache, r_cnn_cache, offset  # type: ignore[return-value]

    def ctc_forward(self, xs, xs_lens=None, n_chunks=None):
        ctc_probs = self.ctc.log_softmax(xs)
        topk_prob, topk_index = ctc_probs.topk(1, dim=2)  # (B, maxlen, 1)
        hyps = topk_index.squeeze(-1)  # (B, maxlen)

        if (n_chunks is not None) and (xs_lens is not None):
            hyps = hyps.split(n_chunks, dim=0)
            hyps = [hyp.flatten()[:x_len] for hyp, x_len in zip(hyps, xs_lens)]
        return hyps
