// user.d.ts
import { Store } from 'pinia';

declare module '../store/user' {
  interface UserState {
    id_number: string;
    role: number;
    balance: number;
  }

  export function useUserStore(): Store<'user', UserState, any, any>;
}