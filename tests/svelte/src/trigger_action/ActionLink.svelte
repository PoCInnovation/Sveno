<script>
    

    

    const handleClick = (e) => {
      e.preventDefault();
      console.log('Le lien a été cliqué.');
    }

</script>

<div>
            <button on:Click={handleClick}>
            Clique ici
            </button>
            <button href="#" on:keypress={handleClick}>
            Clique ici
            </button>
        </div>

<style>
</style>
