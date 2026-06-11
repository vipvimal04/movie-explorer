export interface Genre {
  id: number
  name: string
}

export interface DirectorBrief {
  id: number
  name: string
}

export interface ActorBrief {
  id: number
  name: string
}

export interface Review {
  id: number
  author: string
  rating: number
  comment?: string | null
}

export interface MovieListItem {
  id: number
  title: string
  release_year: number
  rating?: number | null
  director: DirectorBrief
  genres: Genre[]
}

export interface MovieDetail extends MovieListItem {
  description?: string | null
  actors: ActorBrief[]
  reviews: Review[]
}

export interface MovieListResponse {
  items: MovieListItem[]
  total: number
  filters_applied: Record<string, string | number | null>
}

export interface ActorListItem {
  id: number
  name: string
  birth_year?: number | null
}

export interface ActorMovieBrief {
  id: number
  title: string
  release_year: number
  rating?: number | null
}

export interface ActorDetail {
  id: number
  name: string
  bio?: string | null
  birth_year?: number | null
  movies: ActorMovieBrief[]
  genres: Genre[]
}

export interface DirectorListItem {
  id: number
  name: string
  birth_year?: number | null
}

export interface DirectorDetail {
  id: number
  name: string
  bio?: string | null
  birth_year?: number | null
  movies: ActorMovieBrief[]
  genres: Genre[]
}

export interface GenreListResponse {
  items: Genre[]
  total: number
}

export interface ApiError {
  detail: string
}
