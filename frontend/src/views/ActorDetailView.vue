<script setup lang="ts">
import { onMounted, ref, watch } from 'vue'
import { RouterLink } from 'vue-router'

import { api } from '@/api/client'
import EmptyState from '@/components/EmptyState.vue'
import LoadingState from '@/components/LoadingState.vue'
import type { ActorDetail } from '@/types'

const props = defineProps<{
  id: string
}>()

const actor = ref<ActorDetail | null>(null)
const loading = ref(true)
const error = ref('')

async function loadActor() {
  loading.value = true
  error.value = ''
  try {
    actor.value = await api.getActor(Number(props.id))
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'Actor not found'
    actor.value = null
  } finally {
    loading.value = false
  }
}

onMounted(loadActor)
watch(() => props.id, loadActor)
</script>

<template>
  <LoadingState v-if="loading" />

  <EmptyState
    v-else-if="error || !actor"
    title="Actor unavailable"
    :message="error || 'This actor profile could not be loaded.'"
  />

  <section v-else class="space-y-6">
    <div>
      <h1 class="text-3xl font-bold text-white">{{ actor.name }}</h1>
      <p v-if="actor.birth_year" class="mt-2 text-slate-400">Born {{ actor.birth_year }}</p>
    </div>

    <p v-if="actor.bio" class="max-w-3xl text-slate-300">{{ actor.bio }}</p>

    <div class="rounded-xl border border-slate-800 bg-slate-900 p-5">
      <h2 class="font-semibold text-white">Genres</h2>
      <div class="mt-2 flex flex-wrap gap-2">
        <span
          v-for="genre in actor.genres"
          :key="genre.id"
          class="rounded-full bg-slate-800 px-2.5 py-1 text-xs text-slate-300"
        >
          {{ genre.name }}
        </span>
      </div>
    </div>

    <div class="rounded-xl border border-slate-800 bg-slate-900 p-5">
      <h2 class="font-semibold text-white">Filmography</h2>
      <ul v-if="actor.movies.length" class="mt-3 space-y-2">
        <li v-for="movie in actor.movies" :key="movie.id">
          <RouterLink
            :to="{ name: 'movie-detail', params: { id: movie.id } }"
            class="text-amber-400 hover:underline"
          >
            {{ movie.title }} ({{ movie.release_year }})
          </RouterLink>
        </li>
      </ul>
      <p v-else class="mt-2 text-slate-400">No movies listed for this actor.</p>
    </div>
  </section>
</template>
