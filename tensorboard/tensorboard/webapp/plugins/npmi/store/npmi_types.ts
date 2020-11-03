/* Copyright 2020 The TensorFlow Authors. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================*/
import {DataLoadState, LoadState} from '../../../types/data';

export {DataLoadState, LoadState};

export const NPMI_FEATURE_KEY = 'npmi';

type Metric = string;
export type Annotation = string;
export type AnnotationDataListing = Record<Annotation, ValueData[]>;
export type ArithmeticElement =
  | {kind: ArithmeticKind.METRIC; metric: string}
  | {kind: ArithmeticKind.OPERATOR; operator: Operator};
export enum Operator {
  AND,
}
export enum ArithmeticKind {
  METRIC,
  OPERATOR,
}

export interface ValueData {
  nPMIValue: number | null;
  countValue: number | null;
  annotation: Annotation;
  metric: Metric;
  run: string;
}

export interface MetricListing {
  [runId: string]: Metric[];
}

export interface MetricFilterListing {
  [metric: string]: MetricFilter;
}

export interface EmbeddingListing {
  [annotation: string]: number[];
}

export interface MetricFilter {
  max: number;
  min: number;
  includeNaN: boolean;
}

export interface AnnotationSort {
  metric: string;
  order: SortOrder;
}

export enum SortOrder {
  DOWN,
  UP,
}

export interface NpmiState {
  // coming from backend
  pluginDataLoaded: LoadState;
  annotationData: AnnotationDataListing;
  runToMetrics: MetricListing;
  embeddingData: EmbeddingListing;

  // based on user interaction
  selectedAnnotations: Annotation[];
  flaggedAnnotations: Annotation[];
  hiddenAnnotations: Annotation[];
  annotationsRegex: string;
  metricsRegex: string;
  metricArithmetic: ArithmeticElement[];
  metricFilters: MetricFilterListing;
  sort: AnnotationSort;
  pcExpanded: boolean;
  annotationsExpanded: boolean;
  sidebarExpanded: boolean;
  showCounts: boolean;
  showHiddenAnnotations: boolean;
  sidebarWidth: number;
}

export interface State {
  [NPMI_FEATURE_KEY]?: NpmiState;
}

export interface TfColorScale extends HTMLElement {
  runsColorScale?: (runName: string) => string;
}
