import { configureStore } from '@reduxjs/toolkit';
// import featureReducer from '../features/featureName/featureSlice';

export const store = configureStore({
  reducer: {
    // feature: featureReducer,
  },
});

// 타입 정의
export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
