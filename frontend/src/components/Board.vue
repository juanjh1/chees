<script setup lang="ts">
import Cell from "./Cell.vue";
</script>

<template>
	<div class="board">
		<template v-for="i in 64" :key="i">
			<Cell :content="i.toString()" />
		</template>
	</div>
</template>

<style scoped>
.board {
	grid-area: center;

	display: flex;
	flex-wrap: wrap;
	width: var(--board-size);
	height: var(--board-size);

	background: conic-gradient(
		var(--color-even) 90deg,
		var(--color-odd) 90deg 180deg,
		var(--color-even) 180deg 270deg,
		var(--color-odd) 270deg
	);
	background-size: calc(var(--cell-size) * 2) calc(var(--cell-size) * 2);
}
</style>
