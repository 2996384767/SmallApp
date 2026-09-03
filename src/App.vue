<script setup lang="ts">
import { onLaunch, onShow, onHide } from "@dcloudio/uni-app";
onLaunch(() => {
  console.log("App Launch");
});
onShow(() => {
  console.log("App Show");
});
onHide(() => {
  console.log("App Hide");
});
</script>
<style>
page {
  min-height: 100%;
  background: #f5f7fa;
  color: #1f2937;
  font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 28rpx;
}

view,
text,
input,
textarea,
button {
  box-sizing: border-box;
}

button {
  margin: 0;
}

button::after {
  border: 0;
}

.app-card {
  border: 1rpx solid #e5e7eb;
  border-radius: 16rpx;
  background: #ffffff;
}

.app-primary-button {
  width: 100%;
  height: 92rpx;
  border-radius: 16rpx;
  background: #0052d9;
  color: #ffffff;
  font-size: 30rpx;
  font-weight: 600;
  line-height: 92rpx;
}

.app-primary-button[disabled] {
  background: #98a2b3;
  color: #ffffff;
}

.app-text-button {
  padding: 0;
  border: 0;
  background: transparent;
  color: #0052d9;
  font-size: 28rpx;
  line-height: 44rpx;
}
</style>
