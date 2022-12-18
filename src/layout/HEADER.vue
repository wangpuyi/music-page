<template>
	<div id="header1">
	</div>
	<div id="header">
		<div class>
			<img alt="Vue logo" src="../assets/logo.png" width="70" height="70" style=" text-align: center;">
		</div>

		<div class="title">
			<div class="icon"><span class="iconfont icon-yinleyanzou"></span></div>
			<div class="text"><span>MirrorMusic</span></div>
		</div>

		<div class="search" style="float:left">
			<SearchVue />
		</div>
	</div>

</template>


<script>

import SearchVue from '@/components/Search.vue';
export default {
	name: "Header",
	components: { SearchVue },
	data() {
		return {

		};
	},
	methods: {

	},
}
</script>

<style lang="less" scoped>
#header {

	position: fixed;
	display: flex;
	align-items: center;
	width: 100%;
	height: 100px;
	background-color: aquamarine;
	z-index: 99;
	margin-bottom: 10px;

	.search {
		position: relative;
		flex: 2;
		display: flex;
		align-items: center;
		height: 60px;
		margin-left: 10px;

	}

	.title {

		display: flex;

		height: 60px;

		margin-left: 10px;

		.text {
			font-size: 22px;
			color: rgb(207, 70, 70);
			font-family: Arial, Helvetica, sans-serif;
			line-height: 60px;
		}
	}
}
</style>