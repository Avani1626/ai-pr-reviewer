import axios from "axios";

const API_URL = "http://127.0.0.1:8000/review";

export const reviewPR = async (data) => {
  const response = await axios.post(API_URL, data);
  return response.data;
};
