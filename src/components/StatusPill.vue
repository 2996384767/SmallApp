<template>
  <text :class="['status-pill', tone]">{{ label }}</text>
</template>

<script setup lang="ts">
const props = defineProps<{
  status: string
}>()

const statusMap: Record<string, { label: string; tone: string }> = {
  published: { label: "可接单", tone: "info" },
  pending: { label: "待平台审核", tone: "warning" },
  approved: { label: "已通过", tone: "success" },
  completed: { label: "已完成", tone: "success" },
  matched: { label: "已匹配", tone: "success" },
  rejected: { label: "已拒绝", tone: "danger" }
}

const current = statusMap[props.status] || { label: props.status, tone: "muted" }
const label = current.label
const tone = current.tone
</script>

<style scoped>
.status-pill {
  flex: 0 0 auto;
  padding: 6rpx 14rpx;
  border-radius: 8rpx;
  font-size: 22rpx;
  font-weight: 600;
  line-height: 32rpx;
}

.info {
  background: #eff8ff;
  color: #2e90fa;
}

.warning {
  background: #fffaeb;
  color: #f79009;
}

.success {
  background: #ecfdf3;
  color: #12b76a;
}

.danger {
  background: #fff7f6;
  color: #d92d20;
}

.muted {
  background: #f8fafc;
  color: #667085;
}
</style>
