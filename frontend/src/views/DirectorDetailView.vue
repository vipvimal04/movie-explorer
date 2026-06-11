<script setup lang="ts">
import { onMounted, ref, watch } from 'vue'
import { RouterLink } from 'vue-router'

import { api } from '@/api/client'
import EmptyState from '@/components/EmptyState.vue'
import LoadingState from '@/components/LoadingState.vue'
import type { DirectorDetail } from '@/types'

const props = defineProps<{
  id: string
}>()

const director = ref<DirectorDetail | null>(null)
const loading = ref(true)
const error = ref('')

async function loadDirector() {
  loading.value = true
  error.value = ''
  try {
    director.value = await api.getDirector(Number(props.id))
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'Director not found'
    director.value = null
  } finally {
    loading.value = false
  }
}

onMounted(loadDirector)
watch(() => props.id, loadDirector)
</script>

<template>
  <LoadingState v-if="loading" />

  <EmptyState
    v-else-if="error || !director"
    title="Director unavailable"
    :message="error || 'This director profile could not be loaded.'"
  />

  <section v-else class="space-y-6">
    <div>
      <h1 class="text-3xl font-bold text-white">{{ director.name }}</h1>
      <p v-if="director.birth_year" class="mt-2 text-slate-400">Born {{ director.birth_year }}</p>
    </div>

    <p v-if="director.bio" class="max-w-3xl text-slate-300">{{ director.bio }}</p>

    <div class="rounded-xl border border-slate-800 bg-slate-900 p-5">
      <h2 class="font-semibold text-white">Genres</h2>
      <div class="mt-2 flex flex-wrap gap-2">
        <span
          v-for="genre in director.genres"
          :key="genre.id"
          class="rounded-full bg-slate-800 px-2.5 py-1 text-xs text-slate-300"
        >
          {{ genre.name }}
        </span>
      </div>
    </div>

    <div class="rounded-xl border border-slate-800 bg-slate-900 p-5">
      <h2 class="font-semibold text-white">Directed Movies</h2>
      <ul v-if="director.movies.length" class="mt-3 space-y-2">
        <li v-for="movie in director.movies" :key="movie.id">
          <RouterLink
            :to="{ name: 'movie-detail', params: { id: movie.id } }"
            class="text-amber-400 hover:underline"
          >
            {{ movie.title }} ({{ movie.release_year }})
          </RouterLink>
        </li>
      </ul>
      <p v-else class="mt-2 text-slate-400">No movies listed for this director.</p>
    </div>
  </section>
</template>
