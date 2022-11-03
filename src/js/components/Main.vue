<script setup>
import { ref } from 'vue';
import MatrixFill from "./MatrixFill";

const matrizA = ref({
    ren: 0,
    col: 0,
    matrix: []
})

const matrizB = ref({
    ren: 0,
    col: 0,
    matrix: []
})

const proced = ref(false)

function mult(){
    if(matrizA.value.col !== matrizB.value.ren){
        alert('Producto no viable')
        return;
    }
    proced.value = true;
}

</script>

<template>
    <div class="container">
        <form @submit.prevent="mult">
            <div class="row">
                <div class="six columns">
                    <matrix v-model:ren="matrizA.ren" v-model:col="matrizA.col" nombre="A" />
                </div>
                <div class="six columns">
                    <matrix v-model:ren="matrizB.ren" v-model:col="matrizB.col" nombre="B" />

                </div>
            </div>
            <div style="margin-top: 7px">
                <button type="submit">
                    Multiplicar
                </button>
            </div>
        </form>
        <div v-if="proced">
            <div class="six columns">
                <matrix-fill v-model:matrix="matrizA.matrix" :ren="matrizA.ren" :col="matrizA.col" />
            </div>
            <div class="six columns">
                <matrix-fill v-model:matrix="matrizB.matrix" :ren="matrizB.ren" :col="matrizB.col" />
            </div>
        </div>
        <div>

        </div>
    </div>
</template>

<script>
import Matrix from "./Matrix";
export default {
    name: "Main",
    components: {Matrix}
}
</script>

<style scoped>

</style>