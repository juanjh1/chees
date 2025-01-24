<script setup lang="ts">
import Board from "./Board.vue";
import ColumnNumber from "./ColumnNumber.vue";
import RowLetter from "./RowLetter.vue";
</script>

<template>
	<div class="frame">
		<RowLetter position="TOP" />
		<ColumnNumber position="LEFT" />

		<Board />

		<RowLetter position="BOTTOM" />
		<ColumnNumber position="RIGHT" />
	</div>
</template>

<style scoped>
.frame {
	--size: calc(var(--board-size) + var(--cell-size));

	display: grid;
	grid-template-areas:
		"top top top"
		"left center right"
		"bottom bottom bottom";

	width: var(--size);
	height: var(--size);
	background-color: var(--color-frame);
}
</style>
