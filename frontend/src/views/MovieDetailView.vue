<script setup lang="ts">
import { onMounted, ref, watch } from 'vue'
import { RouterLink } from 'vue-router'

import { api } from '@/api/client'
import EmptyState from '@/components/EmptyState.vue'
import LoadingState from '@/components/LoadingState.vue'
import { useFavorites } from '@/composables/useFavorites'
import type { MovieDetail, MovieListItem } from '@/types'

const props = defineProps<{
  id: string
}>()

const movie = ref<MovieDetail | null>(null)
const loading = ref(true)
const error = ref('')
const { isFavorite, toggleFavorite } = useFavorites()

async function loadMovie() {
  loading.value = true
  error.value = ''
  try {
    movie.value = await api.getMovie(Number(props.id))
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'Movie not found'
    movie.value = null
  } finally {
    loading.value = false
  }
}

function asListItem(detail: MovieDetail): MovieListItem {
  return {
    id: detail.id,
    title: detail.title,
    release_year: detail.release_year,
    rating: detail.rating,
    director: detail.director,
    genres: detail.genres,
  }
}

onMounted(loadMovie)
watch(() => props.id, loadMovie)
</script>

<template>
  <LoadingState v-if="loading" />

  <EmptyState
    v-else-if="error || !movie"
    title="Movie unavailable"
    :message="error || 'This movie could not be loaded.'"
  />

  <section v-else class="space-y-6">
    <div class="flex flex-wrap items-start justify-between gap-4">
      <div>
        <h1 class="text-3xl font-bold text-white">{{ movie.title }}</h1>
        <p class="mt-2 text-slate-400">Released {{ movie.release_year }}</p>
      </div>
      <button
        type="button"
        class="rounded-lg bg-amber-500 px-4 py-2 text-sm font-semibold text-slate-900 hover:bg-amber-400"
        @click="toggleFavorite(asListItem(movie))"
      >
        {{ isFavorite(movie.id) ? 'Remove from Watch Later' : 'Add to Watch Later' }}
      </button>
    </div>

    <p v-if="movie.rating" class="text-lg font-medium text-amber-400">
      Rating: {{ movie.rating.toFixed(1) }}
    </p>

    <p class="max-w-3xl text-slate-300">{{ movie.description }}</p>

    <div class="grid gap-6 md:grid-cols-2">
      <div class="rounded-xl border border-slate-800 bg-slate-900 p-5">
        <h2 class="font-semibold text-white">Director</h2>
        <RouterLink
          :to="{ name: 'director-detail', params: { id: movie.director.id } }"
          class="mt-2 inline-block text-amber-400 hover:underline"
        >
          {{ movie.director.name }}
        </RouterLink>
      </div>

      <div class="rounded-xl border border-slate-800 bg-slate-900 p-5">
        <h2 class="font-semibold text-white">Genres</h2>
        <div class="mt-2 flex flex-wrap gap-2">
          <span
            v-for="genre in movie.genres"
            :key="genre.id"
            class="rounded-full bg-slate-800 px-2.5 py-1 text-xs text-slate-300"
          >
            {{ genre.name }}
          </span>
        </div>
      </div>
    </div>

    <div class="rounded-xl border border-slate-800 bg-slate-900 p-5">
      <h2 class="font-semibold text-white">Cast</h2>
      <ul class="mt-3 space-y-2">
        <li v-for="actor in movie.actors" :key="actor.id">
          <RouterLink
            :to="{ name: 'actor-detail', params: { id: actor.id } }"
            class="text-amber-400 hover:underline"
          >
            {{ actor.name }}
          </RouterLink>
        </li>
      </ul>
    </div>

    <div class="rounded-xl border border-slate-800 bg-slate-900 p-5">
      <h2 class="font-semibold text-white">Reviews</h2>
      <ul class="mt-3 space-y-4">
        <li
          v-for="review in movie.reviews"
          :key="review.id"
          class="border-b border-slate-800 pb-3 last:border-0"
        >
          <p class="font-medium text-slate-200">
            {{ review.author }}
            <span class="ml-2 text-amber-400">{{ review.rating.toFixed(1) }}</span>
          </p>
          <p class="mt-1 text-sm text-slate-400">{{ review.comment }}</p>
        </li>
      </ul>
    </div>
  </section>
</template>
