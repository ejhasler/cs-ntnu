package io.javabrains.springbootquickstart.courseapi.course;


import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class CourseController {
    
    @Autowired
    private CourseService courseService;

    @RequestMapping("/topics/{id}")
    public List<Course> getAllCourses(@PathVariable String id) {
        return courseService.getAllCourses();
    }

    @RequestMapping("/topics/{topicId}/courses/{id}")
    public Course getCourse(@PathVariable String id) {
        return courseService.getCourse(id);
    }

    @RequestMapping(method=RequestMethod.POST, value = "/topic")
    public void addTopic(@RequestBody Course topic) {
        topicService.addTopic(topic);
    }

    @RequestMapping(method = RequestMethod.PUT, value = "/topic/{id}")
    public void updateTopic(@RequestBody Course topic, @PathVariable String id) {
        topicService.updateTopic(id, topic);
    }

    @RequestMapping(method = RequestMethod.DELETE, value = "/topic/{id}")
    public void deleteTopic(@PathVariable String id) {
        topicService.getTopic(id);
    }
}
