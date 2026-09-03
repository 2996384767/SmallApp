<template>
  <view class="h5-stage">
    <view class="page-shell">
      <view class="status-bar">
        <text>9:30</text>
        <text class="status-dot">●●●</text>
      </view>
      <view class="nav-bar">
        <text class="nav-title">需求大厅</text>
      </view>
      <view class="content">
        <view class="surface">
          <text class="title">需求大厅</text>
          <text class="desc">登录流程已接入，下一步展示已发布需求和筛选条件。</text>
        </view>
      </view>
    </view>
  </view>
</template>

<script setup lang="ts"></script>

<style scoped>
.h5-stage {
  min-height: 100vh;
  background: #eef2f7;
}

.page-shell {
  min-height: 100vh;
  background: #f5f7fa;
}

/* #ifdef H5 */
.h5-stage {
  padding: 24px 0;
}

.page-shell {
  width: 390px;
  min-height: 844px;
  margin: 0 auto;
  overflow: hidden;
  border: 1px solid #d8dee8;
  border-radius: 24px;
  box-shadow: 0 16px 42px rgba(15, 23, 42, 0.16);
}
/* #endif */

.status-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 48rpx;
  padding: 0 32rpx;
  background: #ffffff;
  color: #1f2937;
  font-size: 22rpx;
  font-weight: 600;
}

.status-dot {
  color: #667085;
  font-size: 18rpx;
  letter-spacing: 4rpx;
}

.nav-bar {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 88rpx;
  border-bottom: 1rpx solid #e5e7eb;
  background: #ffffff;
}

.nav-title {
  color: #1f2937;
  font-size: 32rpx;
  font-weight: 600;
}

.content {
  padding: 40rpx 32rpx;
}

.surface {
  padding: 32rpx;
  border: 1rpx solid #e5e7eb;
  border-radius: 16rpx;
  background: #ffffff;
}

.title {
  display: block;
  color: #1f2937;
  font-size: 32rpx;
  font-weight: 600;
  line-height: 44rpx;
}

.desc {
  display: block;
  margin-top: 12rpx;
  color: #667085;
  font-size: 26rpx;
  line-height: 38rpx;
}
</style>
