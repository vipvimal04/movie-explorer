<script setup lang="ts">
import EmptyState from '@/components/EmptyState.vue'
import MovieCard from '@/components/MovieCard.vue'
import { useFavorites } from '@/composables/useFavorites'

const { favorites } = useFavorites()
</script>

<template>
  <section class="space-y-6">
    <div>
      <h1 class="text-3xl font-bold text-white">Watch Later</h1>
      <p class="mt-2 text-slate-400">
        Your saved movies are stored locally in this browser (no account required).
      </p>
    </div>

    <EmptyState
      v-if="favorites.length === 0"
      title="No saved movies"
      message="Browse movies and click Save to build your watch-later list."
    />

    <div v-else class="grid gap-4 md:grid-cols-2">
      <MovieCard v-for="movie in favorites" :key="movie.id" :movie="movie" />
    </div>
  </section>
</template>
