<script setup lang="ts">
defineProps<{
	row: number;
	col: string;
	color?: string | null;
	type?: string | null;
}>();

const PIECES_PATH: string = "/assets/pieces";
</script>

<template>
	<div class="piece" :data-x="row" :data-y="col">
		<img
			v-if="type && color"
			:src="`${PIECES_PATH}/${color}-${type}.svg`"
			:alt="`${color} ${type}`"
			class="piece__image"
		/>
	</div>
</template>

<style scoped>
.piece {
	color: var(--black);
	display: flex;
	justify-content: center;
	align-items: center;
	width: var(--cell-size);
	height: var(--cell-size);
}

.piece__image {
	width: var(--piece-size);
	height: var(--piece-size);
	aspect-ratio: 1 / 1;
	pointer-events: none;
	user-select: none;
}
</style>
