<script setup lang="ts">
import { RouterLink } from 'vue-router'

import { useFavorites } from '@/composables/useFavorites'
import type { MovieListItem } from '@/types'

defineProps<{
  movie: MovieListItem
}>()

const { isFavorite, toggleFavorite } = useFavorites()
</script>

<template>
  <article class="rounded-xl border border-slate-800 bg-slate-900 p-5 shadow-lg transition hover:border-amber-500/50">
    <div class="flex items-start justify-between gap-3">
      <div>
        <RouterLink
          :to="{ name: 'movie-detail', params: { id: movie.id } }"
          class="text-lg font-semibold text-white hover:text-amber-400"
        >
          {{ movie.title }}
        </RouterLink>
        <p class="mt-1 text-sm text-slate-400">{{ movie.release_year }}</p>
      </div>
      <button
        type="button"
        class="rounded-lg border border-slate-700 px-3 py-1 text-xs font-medium text-slate-200 hover:border-amber-500 hover:text-amber-400"
        @click="toggleFavorite(movie)"
      >
        {{ isFavorite(movie.id) ? 'Saved' : 'Save' }}
      </button>
    </div>

    <p class="mt-3 text-sm text-slate-300">
      Director:
      <RouterLink
        :to="{ name: 'director-detail', params: { id: movie.director.id } }"
        class="text-amber-400 hover:underline"
      >
        {{ movie.director.name }}
      </RouterLink>
    </p>

    <div class="mt-3 flex flex-wrap gap-2">
      <span
        v-for="genre in movie.genres"
        :key="genre.id"
        class="rounded-full bg-slate-800 px-2.5 py-1 text-xs text-slate-300"
      >
        {{ genre.name }}
      </span>
    </div>

    <p v-if="movie.rating" class="mt-3 text-sm font-medium text-amber-400">
      Rating: {{ movie.rating.toFixed(1) }}
    </p>
  </article>
</template>
