{
    useEffect(() => {
        console.log("print this after update");
        return () => {
            console.log("and this on destroy");
        }
    }, [i]);
    return (
        <div>ok</div>
    );
}