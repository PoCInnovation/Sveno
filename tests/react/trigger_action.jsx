function ActionLink() {
    function handleClick(e) {
      e.preventDefault();
      console.log('Le lien a été cliqué.');
    }
  
    return (
        <div>
            <button onClick={handleClick}>
            Clique ici
            </button>
            <button href="#" onKeyPress={handleClick}>
            Clique ici
            </button>
        </div>
    );
  }