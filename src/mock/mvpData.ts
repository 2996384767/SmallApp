export type DemandStatus = "published" | "pending" | "matched"

export type Demand = {
  id: number
  demandNo: string
  country: string
  category: string
  productName: string
  quantity: string
  craft: string
  deliveryDays: string
  fabric: string
  color: string
  status: DemandStatus
  publishedAt: string
}

export type ApplicationStatus = "pending" | "approved" | "completed"

export type Application = {
  id: number
  demandNo: string
  productName: string
  quantity: string
  status: ApplicationStatus
  updatedAt: string
}

export const demands: Demand[] = [
  {
    id: 1,
    demandNo: "DM-HK-202609-001",
    country: "泰国",
    category: "T 恤",
    productName: "高克重纯棉圆领 T 恤",
    quantity: "12,000 件",
    craft: "水浆印花",
    deliveryDays: "28 天",
    fabric: "230g 纯棉",
    color: "黑 / 白 / 藏青",
    status: "published",
    publishedAt: "09-03 09:20"
  },
  {
    id: 2,
    demandNo: "DM-HK-202609-014",
    country: "马来西亚",
    category: "卫衣",
    productName: "连帽拉链卫衣套装",
    quantity: "6,500 件",
    craft: "刺绣 + 罗纹拼接",
    deliveryDays: "35 天",
    fabric: "棉涤抓绒",
    color: "灰 / 米 / 深绿",
    status: "published",
    publishedAt: "09-03 10:05"
  },
  {
    id: 3,
    demandNo: "DM-HK-202609-021",
    country: "阿联酋",
    category: "针织衫",
    productName: "薄款商务针织开衫",
    quantity: "3,800 件",
    craft: "电脑横机",
    deliveryDays: "42 天",
    fabric: "棉粘混纺",
    color: "驼 / 黑 / 海军蓝",
    status: "matched",
    publishedAt: "09-03 11:30"
  }
]

export const applications: Application[] = [
  {
    id: 1,
    demandNo: "DM-HK-202609-001",
    productName: "高克重纯棉圆领 T 恤",
    quantity: "12,000 件",
    status: "pending",
    updatedAt: "09-03 10:18"
  },
  {
    id: 2,
    demandNo: "DM-HK-202608-117",
    productName: "短袖 POLO 衫",
    quantity: "8,400 件",
    status: "approved",
    updatedAt: "09-02 16:45"
  },
  {
    id: 3,
    demandNo: "DM-HK-202608-096",
    productName: "童装针织套装",
    quantity: "5,200 件",
    status: "completed",
    updatedAt: "08-30 14:10"
  }
]
