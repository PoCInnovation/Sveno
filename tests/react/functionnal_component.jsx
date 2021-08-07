import React, { useEffect } from 'react'
import './App.css'

const FCTest = (props) => {
    useEffect(() => {
        console.log("Print this on mount");
    }, [])
    return <h1>Salut, {props.name}</h1>;
}



function FCTest2(props) {
    useEffect(() => {
        console.log("print this on mount");
        return () => {
            console.log("and that on destroy");
        }
    });
    return (
        <div>ok</div>
    );
}


function FCTest2(props) {
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

function test() {

    let i = 0;

}

export default Test;