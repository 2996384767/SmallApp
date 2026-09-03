<template>
  <view class="frame-stage">
    <view class="phone-frame">
      <!-- #ifdef H5 -->
      <view class="status-bar">
        <text>9:30</text>
        <view class="capsule">
          <view class="capsule-dot" />
          <view class="capsule-line" />
        </view>
      </view>
      <view class="nav-bar">
        <view class="nav-side">
          <slot name="left" />
        </view>
        <text class="nav-title">{{ title }}</text>
        <view class="nav-side">
          <slot name="right" />
        </view>
      </view>
      <!-- #endif -->

      <scroll-view :class="['phone-body', showTab ? 'with-tab' : '']" scroll-y>
        <slot />
      </scroll-view>

      <view v-if="showTab" class="tab-bar">
        <view :class="['tab-item', activeTab === 'demands' ? 'active' : '']" @tap="go('/pages/demands/index')">
          <view class="tab-icon list-icon" />
          <text>需求大厅</text>
        </view>
        <view :class="['tab-item', activeTab === 'applications' ? 'active' : '']" @tap="go('/pages/applications/index')">
          <view class="tab-icon doc-icon" />
          <text>我的接单</text>
        </view>
        <view :class="['tab-item', activeTab === 'profile' ? 'active' : '']" @tap="go('/pages/profile/index')">
          <view class="tab-icon user-icon" />
          <text>我的</text>
        </view>
      </view>
    </view>
  </view>
</template>

<script setup lang="ts">
defineProps<{
  title: string
  showTab?: boolean
  activeTab?: "demands" | "applications" | "profile"
}>()

function go(url: string) {
  uni.redirectTo({ url })
}
</script>

<style scoped>
.frame-stage {
  min-height: 100vh;
  background: #eef2f7;
}

.phone-frame {
  min-height: 100vh;
  background: #f5f7fa;
  color: #1f2937;
}

/* #ifdef H5 */
.frame-stage {
  padding: 24px 0;
}

.phone-frame {
  position: relative;
  width: 390px;
  height: 844px;
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

.capsule {
  display: flex;
  align-items: center;
  gap: 10rpx;
  width: 96rpx;
  height: 34rpx;
  padding: 0 12rpx;
  border: 1rpx solid #d0d5dd;
  border-radius: 18rpx;
}

.capsule-dot {
  width: 12rpx;
  height: 12rpx;
  border-radius: 50%;
  background: #667085;
}

.capsule-line {
  flex: 1;
  height: 2rpx;
  background: #d0d5dd;
}

.nav-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 88rpx;
  border-bottom: 1rpx solid #e5e7eb;
  background: #ffffff;
}

.nav-title {
  color: #1f2937;
  font-size: 32rpx;
  font-weight: 600;
  line-height: 44rpx;
}

.nav-side {
  width: 112rpx;
  height: 88rpx;
  display: flex;
  align-items: center;
  justify-content: center;
}

.phone-body {
  height: 100vh;
}

/* #ifdef H5 */
.phone-body {
  height: calc(844px - 68px);
}

.phone-body.with-tab {
  height: calc(844px - 68px - 64px);
}
/* #endif */

.tab-bar {
  display: flex;
  align-items: center;
  height: 128rpx;
  padding-bottom: env(safe-area-inset-bottom);
  border-top: 1rpx solid #e5e7eb;
  background: #ffffff;
}

.tab-item {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 6rpx;
  min-height: 96rpx;
  color: #667085;
  font-size: 22rpx;
  line-height: 30rpx;
}

.tab-item.active {
  color: #0052d9;
  font-weight: 600;
}

.tab-icon {
  position: relative;
  width: 36rpx;
  height: 36rpx;
}

.list-icon {
  border-top: 5rpx solid currentColor;
  border-bottom: 5rpx solid currentColor;
}

.list-icon::after {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  top: 15rpx;
  border-top: 5rpx solid currentColor;
}

.doc-icon {
  border: 4rpx solid currentColor;
  border-radius: 6rpx;
}

.doc-icon::after {
  content: "";
  position: absolute;
  left: 7rpx;
  right: 7rpx;
  top: 11rpx;
  border-top: 4rpx solid currentColor;
  box-shadow: 0 10rpx 0 currentColor;
}

.user-icon::before,
.user-icon::after {
  content: "";
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  border: 4rpx solid currentColor;
}

.user-icon::before {
  top: 0;
  width: 16rpx;
  height: 16rpx;
  border-radius: 50%;
}

.user-icon::after {
  bottom: 0;
  width: 30rpx;
  height: 16rpx;
  border-radius: 16rpx 16rpx 6rpx 6rpx;
}
</style>
