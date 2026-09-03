<template>
  <MiniProgramFrame title="企业登录">
    <view class="login-page">
      <view class="brand-row">
        <view class="brand-mark">SL</view>
        <view class="brand-copy">
          <text class="brand-kicker">肃宁针织产业带</text>
          <text class="brand-title">肃联跨境</text>
          <text class="brand-subtitle">海外需求撮合与订单进度管理</text>
        </view>
      </view>

      <view class="ticket-strip">
        <view class="ticket-line" />
        <view class="ticket-copy">
          <text class="ticket-title">平台审核后发布</text>
          <text class="ticket-text">工厂端只查看脱敏后的需求、数量、工艺和交付周期。</text>
        </view>
      </view>

      <view class="auth-panel app-card">
        <view class="panel-head">
          <view>
            <text class="panel-title">账号登录</text>
            <text class="panel-desc">使用企业账号进入需求大厅</text>
          </view>
          <StatusPill status="published" />
        </view>

        <view :class="['field', errors.account ? 'is-error' : '']">
          <text class="field-label">企业账号</text>
          <input
            v-model="account"
            class="field-input"
            placeholder="请输入企业账号"
            placeholder-class="field-placeholder"
            maxlength="32"
            @input="clearFieldError('account')"
          />
          <text v-if="errors.account" class="field-error">{{ errors.account }}</text>
        </view>

        <view :class="['field', errors.password ? 'is-error' : '']">
          <text class="field-label">登录密码</text>
          <input
            v-model="password"
            class="field-input"
            password
            placeholder="请输入登录密码"
            placeholder-class="field-placeholder"
            maxlength="32"
            @input="clearFieldError('password')"
          />
          <text v-if="errors.password" class="field-error">{{ errors.password }}</text>
        </view>

        <view class="form-tools">
          <label class="remember-row" @tap="remember = !remember">
            <checkbox :checked="remember" color="#0052D9" />
            <text>保持登录</text>
          </label>
          <button class="app-text-button" @tap="goRegister">企业注册</button>
        </view>

        <view v-if="errorMessage" class="form-error">{{ errorMessage }}</view>

        <button
          class="app-primary-button"
          :loading="loading"
          :disabled="!canSubmit || loading"
          @tap="handleLogin"
        >
          登录并查看需求
        </button>

        <view class="demo-account">
          <text class="demo-label">演示账号</text>
          <text class="demo-text">factory001 / 默认演示密码</text>
        </view>
      </view>
    </view>
  </MiniProgramFrame>
</template>

<script setup lang="ts">
import { computed, onMounted, reactive, ref } from "vue"
import MiniProgramFrame from "../../components/MiniProgramFrame.vue"
import StatusPill from "../../components/StatusPill.vue"
import { AUTH_MODE } from "../../config/env"
import { request } from "../../utils/request"

type LoginResult = {
  token: string
  account: string
}

const account = ref("")
const password = ref("")
const remember = ref(true)
const loading = ref(false)
const errorMessage = ref("")
const errors = reactive<Record<string, string>>({})
const canSubmit = computed(() => account.value.trim().length > 0 && password.value.length >= 6)

onMounted(() => {
  const pendingAccount = uni.getStorageSync("pendingAccount")
  if (pendingAccount) {
    account.value = pendingAccount
  }
})

function clearFieldError(field: string) {
  errors[field] = ""
  errorMessage.value = ""
}

function validate() {
  errors.account = account.value.trim() ? "" : "请输入企业账号"
  errors.password = password.value.length >= 6 ? "" : "密码至少 6 位"
  return !errors.account && !errors.password
}

async function handleLogin() {
  if (!validate()) return

  loading.value = true
  errorMessage.value = ""

  try {
    const auth = AUTH_MODE === "mock" ? await mockLogin() : await apiLogin()
    if (remember.value) {
      uni.setStorageSync("token", auth.token)
    }
    uni.setStorageSync("factoryAccount", auth.account)
    uni.redirectTo({ url: "/pages/demands/index" })
  } catch (error) {
    errorMessage.value = error instanceof Error ? error.message : "登录失败，请检查账号和密码"
  } finally {
    loading.value = false
  }
}

function mockLogin(): Promise<LoginResult> {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve({
        token: `mock-token-${Date.now()}`,
        account: account.value.trim() || "factory001"
      })
    }, 420)
  })
}

function apiLogin() {
  return request<LoginResult>({
    url: "/api/login",
    method: "POST",
    data: {
      account: account.value.trim(),
      password: password.value
    }
  })
}

function goRegister() {
  uni.navigateTo({ url: "/pages/auth/register" })
}
</script>

<style scoped>
.login-page {
  padding: 40rpx 32rpx 48rpx;
}

.brand-row {
  display: flex;
  align-items: center;
  gap: 24rpx;
  margin-bottom: 32rpx;
}

.brand-mark {
  width: 96rpx;
  height: 96rpx;
  border-radius: 16rpx;
  background: #0052d9;
  color: #ffffff;
  font-size: 30rpx;
  font-weight: 700;
  line-height: 96rpx;
  text-align: center;
}

.brand-copy {
  min-width: 0;
  display: flex;
  flex-direction: column;
}

.brand-kicker {
  color: #667085;
  font-size: 24rpx;
  line-height: 34rpx;
}

.brand-title {
  margin-top: 4rpx;
  color: #1f2937;
  font-size: 40rpx;
  font-weight: 600;
  line-height: 52rpx;
}

.brand-subtitle {
  margin-top: 4rpx;
  color: #667085;
  font-size: 24rpx;
  line-height: 34rpx;
}

.ticket-strip {
  display: flex;
  margin-bottom: 24rpx;
  overflow: hidden;
  border: 1rpx solid #e5e7eb;
  border-radius: 16rpx;
  background: #ffffff;
}

.ticket-line {
  width: 8rpx;
  background: #0052d9;
}

.ticket-copy {
  flex: 1;
  padding: 20rpx 24rpx;
}

.ticket-title {
  display: block;
  color: #0052d9;
  font-size: 24rpx;
  font-weight: 600;
  line-height: 34rpx;
}

.ticket-text {
  display: block;
  margin-top: 4rpx;
  color: #667085;
  font-size: 24rpx;
  line-height: 36rpx;
}

.auth-panel {
  padding: 32rpx 28rpx;
}

.panel-head {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 24rpx;
  margin-bottom: 30rpx;
}

.panel-title {
  display: block;
  color: #1f2937;
  font-size: 32rpx;
  font-weight: 600;
  line-height: 44rpx;
}

.panel-desc {
  display: block;
  margin-top: 4rpx;
  color: #667085;
  font-size: 24rpx;
  line-height: 34rpx;
}

.field {
  margin-bottom: 24rpx;
}

.field-label {
  display: block;
  margin-bottom: 12rpx;
  color: #1f2937;
  font-size: 28rpx;
  font-weight: 600;
  line-height: 40rpx;
}

.field-input {
  width: 100%;
  height: 88rpx;
  padding: 0 24rpx;
  border: 1rpx solid #e5e7eb;
  border-radius: 16rpx;
  background: #f8fafc;
  color: #1f2937;
  font-size: 28rpx;
}

.field-placeholder {
  color: #98a2b3;
}

.field.is-error .field-input {
  border-color: #d92d20;
  background: #fff7f6;
}

.field-error {
  display: block;
  margin-top: 8rpx;
  color: #d92d20;
  font-size: 24rpx;
  line-height: 34rpx;
}

.form-tools {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin: 4rpx 0 28rpx;
}

.remember-row {
  display: flex;
  align-items: center;
  gap: 8rpx;
  min-height: 48rpx;
  color: #667085;
  font-size: 26rpx;
}

.form-error {
  margin-bottom: 24rpx;
  padding: 18rpx 20rpx;
  border-radius: 16rpx;
  background: #fff7f6;
  color: #d92d20;
  font-size: 24rpx;
  line-height: 36rpx;
}

.demo-account {
  display: flex;
  justify-content: space-between;
  gap: 16rpx;
  margin-top: 24rpx;
  padding-top: 24rpx;
  border-top: 1rpx solid #e5e7eb;
  color: #667085;
  font-size: 24rpx;
  line-height: 34rpx;
}

.demo-label {
  color: #1f2937;
  font-weight: 600;
}

.demo-text {
  text-align: right;
}
</style>
