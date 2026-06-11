<script setup lang="ts">
defineProps<{
  title: string
  message: string
}>()
</script>

<template>
  <div class="rounded-xl border border-dashed border-slate-700 bg-slate-900/50 px-6 py-12 text-center">
    <h3 class="text-lg font-semibold text-slate-200">{{ title }}</h3>
    <p class="mt-2 text-slate-400">{{ message }}</p>
  </div>
</template>
