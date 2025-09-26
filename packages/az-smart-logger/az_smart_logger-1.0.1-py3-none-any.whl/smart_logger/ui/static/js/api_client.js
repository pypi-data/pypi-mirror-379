// api_client.js (global axios version)
const api = axios.create();

api.interceptors.request.use(config => {
    const token = localStorage.getItem("token");
    if (!token) {
        window.location.href = "/auth/login";
        return config;
    }
    config.headers.Authorization = `Bearer ${token}`;
    return config;
}, error => Promise.reject(error));

export default api;