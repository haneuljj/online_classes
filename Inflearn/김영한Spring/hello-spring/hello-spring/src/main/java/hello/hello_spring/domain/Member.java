package hello.hello_spring.domain;

import jakarta.persistence.*;

@Entity
@Table(name = "mem")
public class Member {

    @SequenceGenerator(
            name="mem_seq"
            , sequenceName = "mem_seq"
            , initialValue = 1
            , allocationSize = 1)

    @Id
    @GeneratedValue(generator = "mem_seq")
    private Long id;
    private String name;

    public Long getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public void setName(String name) {
        this.name = name;
    }
}
