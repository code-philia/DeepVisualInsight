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
import {Component, Input} from '@angular/core';
import {from} from 'rxjs';
import {map} from 'rxjs/operators';

import {loadMonaco} from './load_monaco_shim';

/** @typehack */ import * as _typeHackRxjwindowWithRequireAndMonacos from 'rxjs';

// TODO(cais): Explore better typing by depending on external libraries.
const windowWithRequireAndMonaco: any = window;

/**
 * SourceCodeContainer displays the content of a source-code file.
 *
 * It displays the code with visual features including syntax highlighting.
 * It additionally provides functionalities to:
 * - Scroll to and highlight a given line by its line number.
 *
 * TODO(cais): Add support for line decoration and symbol decoration.
 *
 * Unlike SourceFilesComponent, SourceCodeContainer handles only one file at a
 * time.
 */
@Component({
  selector: 'tf-debugger-v2-source-code',
  template: `
    <source-code-component
      [lines]="lines"
      [focusedLineno]="focusedLineno"
      [monaco]="monaco$ | async"
    ></source-code-component>
  `,
})
export class SourceCodeContainer {
  // Lines of the source-code file, split at line breaks.
  @Input()
  lines: string[] | null = null; // TODO(cais): Add spinner for `null`.

  // Line number to scroll to and highlight, 1-based.
  @Input()
  focusedLineno: number | null = null;

  monaco$: any | null = null;

  ngOnInit(): void {
    this.monaco$ = from(loadMonaco()).pipe(
      map(() => windowWithRequireAndMonaco.monaco)
    );
  }

  constructor() {}
}
