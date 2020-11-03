/* Copyright 2019 The TensorFlow Authors. All Rights Reserved.

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
import * as actions from '../actions';
import {reducers} from './core_reducers';
import {
  buildPluginMetadata,
  createEnvironment,
  createPluginMetadata,
  createCoreState,
} from '../testing';
import {DataLoadState} from '../../types/data';
import {PluginsListFailureCode} from '../types';

function createPluginsListing() {
  return {
    core: createPluginMetadata('Core'),
    scalars: createPluginMetadata('Scalars'),
  };
}

describe('core reducer', () => {
  [
    {
      action: actions.changePlugin({plugin: 'bar'}),
    },
    {
      action: actions.pluginUrlHashChanged({plugin: 'bar'}),
    },
  ].forEach(({action}) => {
    describe(action.type, () => {
      it('sets activePlugin to the one in action payload', () => {
        const state = createCoreState({activePlugin: 'foo', plugins: {}});

        const nextState = reducers(state, action);

        expect(nextState.activePlugin).toBe('bar');
      });

      it('does not change plugins when activePlugin changes', () => {
        const state = createCoreState({
          activePlugin: 'foo',
          plugins: createPluginsListing(),
        });

        const nextState = reducers(state, action);

        expect(nextState.plugins).toEqual(createPluginsListing());
      });
    });
  });

  describe('#pluginsListingRequested', () => {
    it('changes the pluginsListLoaded state to LOADING', () => {
      const state = createCoreState({
        pluginsListLoaded: {
          lastLoadedTimeInMs: null,
          state: DataLoadState.NOT_LOADED,
          failureCode: null,
        },
      });
      const nextState = reducers(state, actions.pluginsListingRequested());

      expect(nextState.pluginsListLoaded.state).toEqual(DataLoadState.LOADING);
    });

    it('keeps the lastLoadedTimeInMs the same', () => {
      const state = createCoreState({
        pluginsListLoaded: {
          lastLoadedTimeInMs: 1337,
          state: DataLoadState.NOT_LOADED,
          failureCode: null,
        },
      });
      const nextState = reducers(state, actions.pluginsListingRequested());

      expect(nextState.pluginsListLoaded.lastLoadedTimeInMs).toBe(1337);
    });

    it('keeps the failureCode', () => {
      const state = createCoreState({
        pluginsListLoaded: {
          lastLoadedTimeInMs: null,
          state: DataLoadState.FAILED,
          failureCode: PluginsListFailureCode.NOT_FOUND,
        },
      });
      const nextState = reducers(state, actions.pluginsListingRequested());

      expect(nextState.pluginsListLoaded.failureCode).toEqual(
        PluginsListFailureCode.NOT_FOUND
      );
    });
  });

  describe('#pluginsListingFailed', () => {
    it('changes the pluginsListLoaded state to FAILED', () => {
      const state = createCoreState({
        pluginsListLoaded: {
          lastLoadedTimeInMs: null,
          state: DataLoadState.LOADING,
          failureCode: null,
        },
      });
      const nextState = reducers(
        state,
        actions.pluginsListingFailed({
          failureCode: PluginsListFailureCode.UNKNOWN,
        })
      );

      expect(nextState.pluginsListLoaded.state).toEqual(DataLoadState.FAILED);
    });

    it('keeps the lastLoadedTimeInMs the same', () => {
      const state = createCoreState({
        pluginsListLoaded: {
          lastLoadedTimeInMs: 1337,
          state: DataLoadState.LOADING,
          failureCode: null,
        },
      });
      const nextState = reducers(
        state,
        actions.pluginsListingFailed({
          failureCode: PluginsListFailureCode.UNKNOWN,
        })
      );

      expect(nextState.pluginsListLoaded.lastLoadedTimeInMs).toBe(1337);
    });

    it('sets the failureCode', () => {
      const state = createCoreState({
        pluginsListLoaded: {
          lastLoadedTimeInMs: null,
          state: DataLoadState.LOADING,
          failureCode: null,
        },
      });
      const nextState = reducers(
        state,
        actions.pluginsListingFailed({
          failureCode: PluginsListFailureCode.NOT_FOUND,
        })
      );

      expect(nextState.pluginsListLoaded.failureCode).toEqual(
        PluginsListFailureCode.NOT_FOUND
      );
    });
  });

  describe('#pluginsListingLoaded', () => {
    beforeEach(() => {
      // Angular's zonejs installs mock clock by default. No need for another.
      jasmine.clock().mockDate(new Date(1000));
    });

    it('sets plugins with the payload', () => {
      const state = createCoreState({activePlugin: 'foo', plugins: {}});
      const nextState = reducers(
        state,
        actions.pluginsListingLoaded({plugins: createPluginsListing()})
      );

      expect(nextState.plugins).toEqual(createPluginsListing());
    });

    it('sets the pluginsListLoaded', () => {
      const state = createCoreState({
        activePlugin: 'foo',
        plugins: {},
        pluginsListLoaded: {
          state: DataLoadState.NOT_LOADED,
          lastLoadedTimeInMs: null,
          failureCode: null,
        },
      });
      const nextState = reducers(
        state,
        actions.pluginsListingLoaded({plugins: createPluginsListing()})
      );

      expect(nextState.pluginsListLoaded).toEqual({
        state: DataLoadState.LOADED,
        lastLoadedTimeInMs: 1000,
        failureCode: null,
      });
    });

    it('sets activePlugin to the first enabled plugin when not defined', () => {
      const state = createCoreState({activePlugin: null, plugins: {}});

      const nextState = reducers(
        state,
        actions.pluginsListingLoaded({
          plugins: {
            foo: buildPluginMetadata({tab_name: 'foo', enabled: false}),
            bar: buildPluginMetadata({tab_name: 'bar', enabled: true}),
          },
        })
      );

      expect(nextState.activePlugin).toBe('bar');
    });

    it('sets the plugin to null when nothing is active', () => {
      const state = createCoreState({activePlugin: null, plugins: {}});

      const nextState = reducers(
        state,
        actions.pluginsListingLoaded({
          plugins: {
            foo: buildPluginMetadata({tab_name: 'foo', enabled: false}),
            bar: buildPluginMetadata({tab_name: 'bar', enabled: false}),
          },
        })
      );

      expect(nextState.activePlugin).toBeNull();
    });

    it('does not change activePlugin when already defined', () => {
      const state = createCoreState({activePlugin: 'foo', plugins: {}});

      const nextState = reducers(
        state,
        actions.pluginsListingLoaded({plugins: createPluginsListing()})
      );

      expect(nextState.activePlugin).toBe('foo');
    });

    it('clears the failureCode', () => {
      const state = createCoreState({
        pluginsListLoaded: {
          lastLoadedTimeInMs: null,
          state: DataLoadState.LOADING,
          failureCode: PluginsListFailureCode.UNKNOWN,
        },
      });
      const nextState = reducers(
        state,
        actions.pluginsListingLoaded({plugins: createPluginsListing()})
      );

      expect(nextState.pluginsListLoaded.failureCode).toBeNull();
    });
  });

  describe('#environmentLoaded', () => {
    it('sets environment with the payload', () => {
      const state = createCoreState({
        environment: createEnvironment({data_location: '/original/location'}),
      });
      const nextState = reducers(
        state,
        actions.environmentLoaded({
          environment: createEnvironment({data_location: '/new/location'}),
        })
      );

      expect(nextState.environment.data_location).toEqual('/new/location');
    });
  });

  describe('#toggleReloadEnabled', () => {
    it('toggles reloadEnabled', () => {
      const state1 = createCoreState({reloadEnabled: false});

      const state2 = reducers(state1, actions.toggleReloadEnabled());

      expect(state2.reloadEnabled).toBe(true);

      const state3 = reducers(state2, actions.toggleReloadEnabled());

      expect(state3.reloadEnabled).toBe(false);
    });
  });

  describe('#changeReloadPeriod', () => {
    it('sets the reloadPeriodInMs', () => {
      const state = createCoreState({reloadPeriodInMs: 1});

      const nextState = reducers(
        state,
        actions.changeReloadPeriod({periodInMs: 1000})
      );

      expect(nextState.reloadPeriodInMs).toBe(1000);
    });

    it('ignores the action when periodInMs is non-positive', () => {
      const baseState = createCoreState({reloadPeriodInMs: 1});

      const state1 = reducers(
        baseState,
        actions.changeReloadPeriod({periodInMs: 0})
      );
      expect(state1.reloadPeriodInMs).toBe(1);

      const state2 = reducers(
        baseState,
        actions.changeReloadPeriod({periodInMs: -1000})
      );
      expect(state2.reloadPeriodInMs).toBe(1);
    });
  });

  describe('#fetchRunSucceeded', () => {
    it('sets polymerInteropRuns', () => {
      const state = createCoreState({polymerInteropRuns: []});

      const nextState = reducers(
        state,
        actions.fetchRunSucceeded({
          runs: [
            {id: '1', name: 'Run name 1'},
            {id: '2', name: 'Run name 2'},
          ],
        })
      );

      expect(nextState.polymerInteropRuns).toEqual([
        {id: '1', name: 'Run name 1'},
        {id: '2', name: 'Run name 2'},
      ]);
    });
  });

  describe('#polymerInteropRunSelectionChanged', () => {
    it('changes the polymerInteropRunSelection', () => {
      const state = createCoreState({
        polymerInteropRuns: [
          {id: '1', name: 'Run name 1'},
          {id: '2', name: 'Run name 2'},
          {id: '3', name: 'Run name 3'},
          {id: '4', name: 'Run name 4'},
        ],
        polymerInteropRunSelection: new Set(),
      });

      const nextState = reducers(
        state,
        actions.polymerInteropRunSelectionChanged({
          nextSelection: ['1', '2', '4'],
        })
      );

      expect(nextState.polymerInteropRunSelection).toEqual(
        new Set(['1', '2', '4'])
      );
    });
  });
});
