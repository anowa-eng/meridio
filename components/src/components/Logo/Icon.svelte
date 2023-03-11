<script>
    import { writable } from "svelte/store";

    export let fill;
    export let logoSideLength;
    export var svgRef = writable();
    
    const iconHeight = 65;
    const iconWidth = 65;
</script>

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 65 65" width={logoSideLength} height={logoSideLength} bind:this={svgRef}>
    <path {fill} d="M 15 0 l 15 15 l -15 15 l -15 -15 z" transform="translate(17.5 0)" />
    <path {fill} d="M 15 0 l 15 15 l -15 15 l -15 -15 z" transform="translate(0 17.5)" />
    <path {fill} d="M 15 0 l 15 15 l -15 15 l -15 -15 z" transform="translate(35 17.5)" />
    <path {fill} d="M 15 0 l 15 15 l -15 15 l -15 -15 z" transform="translate(17.5 35)" />
</svg>
