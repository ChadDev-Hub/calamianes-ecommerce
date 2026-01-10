const API_BASE = process.env.NEXT_PUBLIC_API_ROUTER;
export const homepageData = {
  data: async () => await fetch(`${API_BASE}/`).then(res => res.json()),
};