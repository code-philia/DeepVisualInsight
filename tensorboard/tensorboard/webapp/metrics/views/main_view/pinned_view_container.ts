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
import {ChangeDetectionStrategy, Component, Input} from '@angular/core';
import {Store} from '@ngrx/store';
import {Observable} from 'rxjs';
import {startWith} from 'rxjs/operators';

import {State} from '../../../app_state';
import {DeepReadonly} from '../../../util/types';
import {getPinnedCardsWithMetadata} from '../../store';
import {CardObserver} from '../card_renderer/card_lazy_loader';
import {CardIdWithMetadata} from '../metrics_view_types';

@Component({
  selector: 'metrics-pinned-view',
  template: `
    <metrics-pinned-view-component
      [cardIdsWithMetadata]="cardIdsWithMetadata$ | async"
      [cardObserver]="cardObserver"
    ></metrics-pinned-view-component>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class PinnedViewContainer {
  @Input() cardObserver!: CardObserver;

  constructor(private readonly store: Store<State>) {}

  readonly cardIdsWithMetadata$: Observable<
    DeepReadonly<CardIdWithMetadata[]>
  > = this.store.select(getPinnedCardsWithMetadata).pipe(startWith([]));
}
