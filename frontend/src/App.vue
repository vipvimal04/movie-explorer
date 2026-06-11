<script setup lang="ts">
import AppNav from '@/components/AppNav.vue'
</script>

<template>
  <div class="min-h-screen bg-slate-950">
    <AppNav />
    <main class="mx-auto max-w-6xl px-4 py-8">
      <RouterView />
    </main>
  </div>
</template>
