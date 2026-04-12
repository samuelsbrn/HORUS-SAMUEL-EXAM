import { reactive } from 'vue';

export const authState = reactive({
  token: localStorage.getItem('token') || null,
  
  setToken(newToken) {
    this.token = newToken;
    localStorage.setItem('token', newToken);
  },
  
  logout() {
    this.token = null;
    localStorage.removeItem('token');
  },
  
  isAuthenticated() {
    return !!this.token;
  }
});