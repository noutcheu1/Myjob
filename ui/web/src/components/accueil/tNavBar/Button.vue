<template>
    <button class ="button">
        {{ message }}
    </button>
</template>
<style>
    .button {
        box-sizing:border-box;
        padding: 7px;
        padding-left: 5px;
        padding-right: 5px;
        width:59px;
        background-color:#FFC947;
        border-radius: 0.4em;
        border: none;
        color: black;
        font-weight: bold;
        font-size: 13px;
        cursor: pointer;
    }
    .button:hover {
        background-color:#10345D
    }
    .button:focus {
        box-shadow: 0px 0px 0px 4px lightblue;
    }
</style>
<script>
export default {
  name: 'Button',
  props: {
    message: String
  }
}
</script>
