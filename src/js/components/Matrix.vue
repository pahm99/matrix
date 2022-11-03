<script setup>
import { ref } from 'vue';
const props = defineProps({
    nombre: String,
    ren: Number,
    col: Number
})

const emit = defineEmits([
    'update:ren',
    'update:col'
])

const me_ren = ref(0);
const me_col = ref(0);

function upRen(){
    emit('update:ren',me_ren.value);
}

function upCol(){
    emit('update:col',me_col.value);
}

</script>

<template>
    <div class="card">
        Matrix {{ nombre }}
        <div class="flex">
            <div>
                <label :for="'ren_' + nombre">Renglones</label>
                <input v-model.number="me_ren" class="u-full-width" @input="upRen"
                       type="number" :name="'ren_' + nombre" :id="'ren_' + nombre" required>
            </div>
            <div>
                <label for="col_a">Columnas</label>
                <input v-model.number=me_col class="u-full-width" @input="upCol"
                       type="number" :name="'col_' + nombre" :id="'col_' + nombre" required>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  name: "Matrix"
}
</script>

<style scoped>

</style>