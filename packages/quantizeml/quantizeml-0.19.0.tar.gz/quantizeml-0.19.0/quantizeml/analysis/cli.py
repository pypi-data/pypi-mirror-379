#!/usr/bin/env python
# ******************************************************************************
# Copyright 2024 Brainchip Holdings Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ******************************************************************************
"""
quantizeml analysis main command-line interface.
"""

import argparse

from .. import load_model
from .kernel_distribution import plot_kernel_distribution
from .quantization_error_api import (measure_layer_quantization_error,
                                     measure_cumulative_quantization_error,
                                     measure_weight_quantization_error)
from .tools import print_metric_table


def add_analysis_arguments(parser):
    asp = parser.add_subparsers(dest="analysis_action")

    # Common arguments
    a_parent_parser = argparse.ArgumentParser(add_help=False)
    a_parent_parser.add_argument("-m", "--model", type=str, required=True, help="Model to analyze")

    # Plot kernel distribution
    k_parser = asp.add_parser("kernel_distribution", parents=[a_parent_parser],
                              help="Plot kernel distribution")
    k_parser.add_argument("-l", "--logdir", type=str, required=True,
                          help="Log directory to save plots")

    # Layer quantization error
    qe_parser = asp.add_parser("quantization_error", parents=[a_parent_parser],
                               help="Measure quantization error")
    qe_parser.add_argument("mode", choices=["single", "cumulative", "weight"], default="single",
                           help="Type of error to be computed. Defaults to %(default)s.")
    qe_parser.add_argument("-fm", "--float_model", type=str, default=None,
                           help="The base model (float version). Defaults to %(default)s.")
    qe_parser.add_argument("-tl", "--target_layer", type=str, default=None,
                           help="Compute per_channel error for a specific layer/node. "
                           "Defaults to %(default)s.")
    qe_parser.add_argument("-bs", "--batch_size", type=int, default=16,
                           help="Batch size to generate samples. Defaults to %(default)s")
    return [k_parser, qe_parser]


def check_quantization_error_arguments(parser, args):
    if args.mode != "weight" and args.float_model is None:
        parser.error(f"-fm/--float_model argument is required when mode={args.mode}.")


def main(parsers, args):
    """ CLI entry point.

    Contains an argument parser with specific arguments to analysis a model.
    Complete arguments lists available using the -h or --help argument.

    """
    model = load_model(args.model)
    if args.analysis_action == "kernel_distribution":
        plot_kernel_distribution(model, logdir=args.logdir)
    elif args.analysis_action == "quantization_error":
        check_quantization_error_arguments(parsers[1], args)
        if args.mode == "cumulative":
            fmodel = load_model(args.float_model)
            summary = measure_cumulative_quantization_error(fmodel,
                                                            model,
                                                            batch_size=args.batch_size,
                                                            target_layer=args.target_layer)
        elif args.mode == "single":
            fmodel = load_model(args.float_model)
            summary = measure_layer_quantization_error(fmodel,
                                                       model,
                                                       batch_size=args.batch_size,
                                                       target_layer=args.target_layer)
        else:
            summary = measure_weight_quantization_error(model, target_layer=args.target_layer)
        model_name = model.name if hasattr(model, "name") else model.graph.name
        print_metric_table(summary, model_name=model_name)
    else:
        raise RuntimeError(f'unknown action: {args.action}')
