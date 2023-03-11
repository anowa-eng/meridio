<script>
    import { writable } from "svelte/store";
    import Logo from "./Logo.svelte";
    
    let fill = writable('white'), isHovered = writable(false);
    fill.set('white');
</script>

<nav>
    <a href="/">
        <Logo logoSize="full" navbar />
    </a>
    <a href="/">Home</a>
    <a href="/explore">Explore</a>
</nav>

<style>
    @import '@fontsource/inter';
    
    nav {
        display: flex;
        align-items: center;
        
        background: #9C4242;
        
        padding: 9px 55px;
    }
    a {
        font-family: Inter;
        font-size: 10pt;
        
        color: white;
        text-decoration: none;
        
        display: flex;
        padding: 0 25px;
        
        transition: color 150ms !important;
    }
    a:hover {
        color: #ff8e8e;
    }
</style>