<script setup lang="ts">
import { onMounted, ref } from 'vue'

import { api } from '@/api/client'
import EmptyState from '@/components/EmptyState.vue'
import LoadingState from '@/components/LoadingState.vue'
import MovieCard from '@/components/MovieCard.vue'
import MovieFilters from '@/components/MovieFilters.vue'
import type { MovieListItem } from '@/types'

const movies = ref<MovieListItem[]>([])
const total = ref(0)
const loading = ref(true)
const error = ref('')

const genre = ref('')
const director = ref('')
const year = ref('')
const actor = ref('')

async function loadMovies() {
  loading.value = true
  error.value = ''
  try {
    const response = await api.getMovies({
      genre: genre.value,
      director: director.value,
      year: year.value,
      actor: actor.value,
    })
    movies.value = response.items
    total.value = response.total
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'Failed to load movies'
    movies.value = []
    total.value = 0
  } finally {
    loading.value = false
  }
}

function resetFilters() {
  genre.value = ''
  director.value = ''
  year.value = ''
  actor.value = ''
  loadMovies()
}

onMounted(loadMovies)
</script>

<template>
  <section class="space-y-6">
    <div>
      <h1 class="text-3xl font-bold text-white">Browse Movies</h1>
      <p class="mt-2 text-slate-400">
        Filter by genre, director, release year, or actor. All filtering is handled by the API.
      </p>
    </div>

    <MovieFilters
      v-model:genre="genre"
      v-model:director="director"
      v-model:year="year"
      v-model:actor="actor"
      @search="loadMovies"
      @reset="resetFilters"
    />

    <p v-if="error" class="rounded-lg border border-red-800 bg-red-950/40 px-4 py-3 text-red-300">
      {{ error }}
    </p>

    <LoadingState v-if="loading" />

    <template v-else>
      <p class="text-sm text-slate-400">{{ total }} movie(s) found</p>

      <EmptyState
        v-if="total === 0"
        title="No movies found"
        message="Try adjusting your filters or reset to see all available movies."
      />

      <div v-else class="grid gap-4 md:grid-cols-2">
        <MovieCard v-for="movie in movies" :key="movie.id" :movie="movie" />
      </div>
    </template>
  </section>
</template>
