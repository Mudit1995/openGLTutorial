#version 330 core

layout (location = 0) out vec4 out_color;

in vec2 uv_0;
in vec3 normal;
in vec3 fragPos ;

struct Light {
    vec3 position;
    vec3 Ia;
    vec3 Id;
    vec3 Is;
};

uniform Light light ; 
uniform sampler2D u_texture_0;

uniform vec3 camPos;

vec3 getLight(vec3 color){
    vec3 Normal = normalize(normal);
    vec3 ambient = light.Ia * color;

    vec3 lightDir = normalize(light.position - fragPos);
    float diff = max(dot(lightDir, Normal), 0.0);
    vec3 diffuse = light.Id * diff ;

    vec3 viewDir = normalize(camPos-fragPos);
    vec3 reflectDir = reflect(-lightDir, Normal);
    float spec = pow(max(dot(viewDir, reflectDir), 0.0), 60.0);
    vec3 specular = light.Is * spec;
    return color * (ambient + diffuse + specular);
}

void main() {
    vec3 color = texture(u_texture_0, uv_0).rgb;
    color = getLight(color);
    out_color = vec4(color, 1.0);
}
