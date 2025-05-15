import axios from 'axios';

const API_URL = 'https://integrative-programming.onrender.com/api/sensor-reading/';

const api = axios.create({ baseURL: API_URL });

export const setAuthToken = (token) => {
  if (token) api.defaults.headers.common['Authorization'] = `Token ${token}`;
  else delete api.defaults.headers.common['Authorization'];
};

export default api;