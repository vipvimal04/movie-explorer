<script setup lang="ts">
import { RouterLink } from 'vue-router'

import { useFavorites } from '@/composables/useFavorites'

const { favorites } = useFavorites()
</script>

<template>
  <header class="border-b border-slate-800 bg-slate-900/80 backdrop-blur">
    <nav class="mx-auto flex max-w-6xl items-center justify-between px-4 py-4">
      <RouterLink to="/" class="text-xl font-bold text-amber-400 hover:text-amber-300">
        Movie Explorer
      </RouterLink>
      <div class="flex items-center gap-4 text-sm">
        <RouterLink to="/" class="text-slate-300 hover:text-white">Browse</RouterLink>
        <RouterLink to="/favorites" class="text-slate-300 hover:text-white">
          Watch Later
          <span
            v-if="favorites.length"
            class="ml-1 rounded-full bg-amber-500 px-2 py-0.5 text-xs font-semibold text-slate-900"
          >
            {{ favorites.length }}
          </span>
        </RouterLink>
      </div>
    </nav>
  </header>
</template>
