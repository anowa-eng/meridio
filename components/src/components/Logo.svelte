<script>
    import { onMount } from "svelte";
    import FullLogo from "./Logo/FullLogo.svelte";
    import Icon from "./Logo/Icon.svelte";
    
    export let logoSize;
    export let logoHeight = null;
    export let navbar = false;
    export let fill = null;
    
    let isHovered, logo;
    onMount(() => {
        console.log(logo.svgRef);
        logo.svgRef.addEventListener('mouseenter', () => (isHovered = true));
        logo.svgRef.addEventListener('mouseleave', () => (isHovered = false));
    })
</script>

{#if logoSize == "full"}
    <FullLogo logoHeight={logoHeight ?? (520 / 27)} fill={!navbar ? (fill ?? '#000') : (isHovered ? '#ff8e8e' : 'white')} bind:this={logo} />
{:else if logoSize == "icon"}
    <Icon logoSideLength={logoHeight ?? (520 / 27)} fill={fill ?? '#000'} bind:this={logo} />
{/if}