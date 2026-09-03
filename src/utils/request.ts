import { API_BASE_URL } from "../config/env"

type RequestOptions = {
  url: string
  method?: "GET" | "POST" | "PUT" | "DELETE"
  data?: Record<string, unknown>
}

export function request<T = unknown>(options: RequestOptions): Promise<T> {
  const token = uni.getStorageSync("token")

  return new Promise((resolve, reject) => {
    uni.request({
      url: `${API_BASE_URL}${options.url}`,
      method: options.method || "GET",
      data: options.data || {},
      header: {
        "content-type": "application/json",
        ...(token ? { Authorization: `Bearer ${token}` } : {})
      },
      success(res) {
        if (res.statusCode && res.statusCode >= 200 && res.statusCode < 300) {
          resolve(res.data as T)
          return
        }

        const data = res.data as { message?: string } | undefined
        reject(new Error(data?.message || "请求失败"))
      },
      fail() {
        reject(new Error("网络不可用，请稍后再试"))
      }
    })
  })
}
