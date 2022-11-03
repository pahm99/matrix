<script setup>
import {computed, ref} from 'vue';
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


const valido = computed(e => matrizA.value.ren > 0 && matrizA.value.col > 0 && matrizB.value.ren > 0 && matrizA.value.col >  0)

const proced = ref(false)

const matrixJSON = ref('');

const procedPy = ref(false)

function mult(){
    if(matrizA.value.col !== matrizB.value.ren){
        alert('Producto no viable')
        return;
    }
    proced.value = true;
    procedPy.value = true;
}

function runPy(){
    matrixJSON.value = JSON.stringify({
        a: {...matrizA.value},
        b: {...matrizB.value}
    });
    document.querySelector('#pybtn').style.visibility = null;
    procedPy.value = true;
}

</script>

<template>
    <div class="container">
        <form @submit.prevent="mult">
            <div class="row">
                <div class="six columns">
                    <matrix :proced="proced" v-model:ren="matrizA.ren" v-model:col="matrizA.col" nombre="A" />
                </div>
                <div class="six columns">
                    <matrix :proced="proced" v-model:ren="matrizB.ren" v-model:col="matrizB.col" nombre="B" />

                </div>
            </div>
            <div style="margin-top: 7px">
                <button :disabled="!valido" type="submit">
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
            <div>
                <button @click.prevent="runPy">Prepara Python</button>
            </div>
        </div>

        <div v-if="procedPy">
            <div id="matrix-json" style="visibility: hidden">
                {{ matrixJSON }}
            </div>
            <div>

            </div>
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