<template>
    <button class ="buttonUp">
        {{ message }}
    </button>
</template>
<style>
    .buttonUp {
        padding: 10px;
        padding-left: 15px;
        padding-right: 15px;
        background-color:#FFC947;
        border-radius: 0.4em;
        border: none;
        color: rgb(40, 40, 40);
        font-weight: bold;
        font-size: 16px;
        cursor: pointer;
    }
    .buttonUp:hover {
        background-color:#10345D
    }
    .buttonUp:focus {
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
