{
    useEffect(() => {
        console.log("Print this on mount");
    }, [])
    return (
        <h1>Salut, {props.name}</h1>
    );
}