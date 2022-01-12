<template>
    <select class = "DropDownList">
        <option> English </option>
        <option> French </option>
    </select>
</template>
<style>
    .DropDownList {
        box-sizing:border-box;
        padding: 4px;
        padding-right: 8px;
        width: 164px;
        background-color:transparent;
        border: solid 2px #DFE1E6;
        color: #888989;
        font-size: 15px;
        -moz-appearance: none;
        -webkit-appearance: none;
        background-size: 10%;
        background-repeat: no-repeat;
        background-position: right;
        background-origin: content-box;
        background-image: url('./image/down_arrow.svg');
    }
    .DropDownList::-ms-expand {
        display: none;
    }
</style>
