<script setup lang="ts">
defineProps<{ content: string }>();
</script>

<template>
	<div class="cell">{{ content }}</div>
</template>

<style scoped>
.cell {
	color: var(--black);
	display: flex;
	justify-content: center;
	align-items: center;
	width: var(--cell-size);
	height: var(--cell-size);
}
</style>
