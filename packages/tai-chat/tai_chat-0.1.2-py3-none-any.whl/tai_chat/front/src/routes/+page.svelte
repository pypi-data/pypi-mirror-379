<script lang="ts">
  import { onMount } from 'svelte';
  import { authStore } from '$lib/stores';
  import { Layout, Login, ChatComponent } from '$lib';

  let isAuthenticated = $state(false);
  let isClient = $state(false);

  onMount(() => {
    isClient = true;
    const unsubscribe = authStore.subscribe(auth => {
      isAuthenticated = auth.isAuthenticated;
    });

    return unsubscribe;
  });

  function handleLoginSuccess() {
    // The auth store will be updated automatically by the Login component
  }
</script>

<Layout>
  {#if isClient}
    {#if isAuthenticated}
      <ChatComponent />
    {:else}
      <Login onLoginSuccess={handleLoginSuccess} />
    {/if}
  {:else}
    <!-- Server-side: show login by default -->
    <Login onLoginSuccess={handleLoginSuccess} />
  {/if}
</Layout>
