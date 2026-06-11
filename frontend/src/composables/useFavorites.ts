import { computed, ref } from 'vue'

import type { MovieListItem } from '@/types'

const STORAGE_KEY = 'movie-explorer-favorites'

function loadFavorites(): MovieListItem[] {
  try {
    const raw = localStorage.getItem(STORAGE_KEY)
    return raw ? (JSON.parse(raw) as MovieListItem[]) : []
  } catch {
    return []
  }
}

const favorites = ref<MovieListItem[]>(loadFavorites())

function persist() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(favorites.value))
}

/** Manage a watch-later list persisted in local storage. */
export function useFavorites() {
  const favoriteIds = computed(() => new Set(favorites.value.map((movie) => movie.id)))

  function isFavorite(movieId: number): boolean {
    return favoriteIds.value.has(movieId)
  }

  function toggleFavorite(movie: MovieListItem): void {
    if (isFavorite(movie.id)) {
      favorites.value = favorites.value.filter((item) => item.id !== movie.id)
    } else {
      favorites.value = [...favorites.value, movie]
    }
    persist()
  }

  function removeFavorite(movieId: number): void {
    favorites.value = favorites.value.filter((item) => item.id !== movieId)
    persist()
  }

  return {
    favorites,
    isFavorite,
    toggleFavorite,
    removeFavorite,
  }
}
