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
import {Component, ChangeDetectionStrategy, Input} from '@angular/core';
import {select, Store} from '@ngrx/store';

import {map} from 'rxjs/operators';

import {State} from '../../../../store/npmi_types';
import {getMetricFilters} from '../../../../store';
import * as npmiActions from '../../../../actions';

/** @typehack */ import * as _typeHackRxjs from 'rxjs';

@Component({
  selector: 'npmi-metric-arithmetic-element',
  template: `
    <metric-arithmetic-element-component
      [metric]="metric"
      [filterValues]="filterValues$ | async"
      (onRemove)="remove($event)"
      (onFilterChange)="filterChange($event)"
    ></metric-arithmetic-element-component>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class MetricArithmeticElementContainer {
  @Input() metric!: string;
  readonly filterValues$ = this.store.pipe(select(getMetricFilters)).pipe(
    map((filters) => {
      const filter = filters[this.metric];
      if (!filter) {
        return {min: -1.0, max: 1.0};
      }
      const min = filter.includeNaN
        ? 'NaN'
        : this.roundToThreeDecimalPoints(filter.min);
      const max =
        filter.max < filter.min
          ? 'NaN'
          : this.roundToThreeDecimalPoints(filter.max);
      return {min: min, max: max};
    })
  );

  constructor(private readonly store: Store<State>) {}

  remove(metric: string) {
    this.store.dispatch(npmiActions.npmiRemoveMetricFilter({metric: metric}));
  }

  filterChange(newValues: {min: number; max: number}) {
    const min = isNaN(newValues.min) ? -1 : newValues.min;
    const max = isNaN(newValues.max) ? -2 : newValues.max;
    const includeNaN = isNaN(newValues.min);
    this.store.dispatch(
      npmiActions.npmiChangeMetricFilter({
        metric: this.metric,
        max: max,
        min: min,
        includeNaN: includeNaN,
      })
    );
  }

  private roundToThreeDecimalPoints(value: number): number {
    return Math.round((value + Number.EPSILON) * 1000) / 1000;
  }
}
