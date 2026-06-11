<script setup lang="ts">
import { onMounted, ref } from 'vue'

import { api } from '@/api/client'
import type { DirectorListItem, Genre } from '@/types'

const genre = defineModel<string>('genre', { default: '' })
const director = defineModel<string>('director', { default: '' })
const year = defineModel<string>('year', { default: '' })
const actor = defineModel<string>('actor', { default: '' })

defineEmits<{
  search: []
  reset: []
}>()

const genres = ref<Genre[]>([])
const directors = ref<DirectorListItem[]>([])

onMounted(async () => {
  const [genreResponse, directorResponse] = await Promise.all([
    api.getGenres(),
    api.getDirectors(),
  ])
  genres.value = genreResponse.items
  directors.value = directorResponse.items
})
</script>

<template>
  <form
    class="grid gap-4 rounded-xl border border-slate-800 bg-slate-900 p-5 md:grid-cols-4"
    @submit.prevent="$emit('search')"
  >
    <label class="flex flex-col gap-1 text-sm">
      <span class="text-slate-400">Genre</span>
      <select
        v-model="genre"
        class="rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-white"
      >
        <option value="">All genres</option>
        <option v-for="item in genres" :key="item.id" :value="item.name">
          {{ item.name }}
        </option>
      </select>
    </label>

    <label class="flex flex-col gap-1 text-sm">
      <span class="text-slate-400">Director</span>
      <select
        v-model="director"
        class="rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-white"
      >
        <option value="">All directors</option>
        <option v-for="item in directors" :key="item.id" :value="item.name">
          {{ item.name }}
        </option>
      </select>
    </label>

    <label class="flex flex-col gap-1 text-sm">
      <span class="text-slate-400">Release year</span>
      <input
        v-model="year"
        type="number"
        min="1888"
        max="2100"
        placeholder="e.g. 2010"
        class="rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-white"
      />
    </label>

    <label class="flex flex-col gap-1 text-sm">
      <span class="text-slate-400">Actor</span>
      <input
        v-model="actor"
        type="text"
        placeholder="Actor name"
        class="rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-white"
      />
    </label>

    <div class="flex gap-3 md:col-span-4">
      <button
        type="submit"
        class="rounded-lg bg-amber-500 px-4 py-2 text-sm font-semibold text-slate-900 hover:bg-amber-400"
      >
        Apply filters
      </button>
      <button
        type="button"
        class="rounded-lg border border-slate-700 px-4 py-2 text-sm text-slate-200 hover:border-slate-500"
        @click="$emit('reset')"
      >
        Reset
      </button>
    </div>
  </form>
</template>
